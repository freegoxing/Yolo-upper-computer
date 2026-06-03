import queue

import cv2
import numpy as np
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage
from ultralytics import YOLO

try:
    from config.yolo_config import CLASS_NAMES, CONF_THRESHOLD, IOU_THRESHOLD
except ImportError:
    from config.yolo_config import CLASS_NAMES, CONF_THRESHOLD, IOU_THRESHOLD


class YoloThread(QThread):
    # 定义信号：发送原始画面
    raw_frame_signal = Signal(QImage)
    # 定义信号：发送处理后的画面
    frame_signal = Signal(QImage)
    # 定义信号：发送检测到的结果信息 (类别数, 目标总数, FPS)
    stats_signal = Signal(int, int, float)
    # 定义信号：发送详细的检测结果列表 (用于 UI 显示详细列表或保存报表)
    results_signal = Signal(list)

    def __init__(self):
        super().__init__()
        self.model = None
        self.source = None  # 输入源 (0, 'video.mp4', 'image.jpg')
        self.is_running = True
        self.conf_threshold = CONF_THRESHOLD
        self.iou_threshold = IOU_THRESHOLD
        self.device = "intel:gpu"  # 默认设备
        self.frame_queue = queue.Queue(maxsize=2)  # 用于 UDP 模式的帧队列
        self.imgsz = 640  # 默认推理尺寸

    def load_model(self, model_path):
        try:
            self.model = YOLO(model_path, task="detect")
            # 预热模型：使用 numpy 生成全黑背景进行预热，避免文件路径问题
            dummy_img = np.zeros((self.imgsz, self.imgsz, 3), dtype=np.uint8)
            self.model.predict(
                source=dummy_img, device=self.device, imgsz=self.imgsz, verbose=False
            )
            return True
        except Exception as e:
            print(f"Error loading model: {e}")
            return False

    def push_frame(self, frame_bgr):
        """供外部（如 UDP 线程）推送帧到队列"""
        if not self.frame_queue.full():
            self.frame_queue.put(frame_bgr)

    def run(self):
        if self.model is None:
            return

        self.is_running = True

        # 统一使用消费者模式：从队列中获取帧进行预测
        # 无论是来自本地视频线程、UDP 线程还是摄像头，都通过 push_frame 喂入
        while self.is_running:
            try:
                # 使用 timeout 避免死锁，允许检查 is_running 状态
                frame_bgr = self.frame_queue.get(timeout=0.1)

                results = self.model.predict(
                    source=frame_bgr,
                    conf=self.conf_threshold,
                    iou=self.iou_threshold,
                    device=self.device,
                    imgsz=self.imgsz,
                    half=True,
                    verbose=False,
                )

                if results and self.is_running:
                    self.emit_result_signals(results[0])

                self.frame_queue.task_done()
            except queue.Empty:
                continue
            except Exception as e:
                print(f"Inference error: {e}")
                continue

    def emit_result_signals(self, result):
        # 1. 获取原始图片和绘制了检测框的图片 (numpy array)
        orig_frame = result.orig_img

        # --- 性能优化：缩放图像以减少 UI 传输和渲染开销 ---
        # 即使原始视频是 1080p，UI 标签通常只有几百像素，缩放到 640 或 800 足矣
        target_ui_width = 800
        h, w = orig_frame.shape[:2]
        if w > target_ui_width:
            scale = target_ui_width / w
            target_ui_height = int(h * scale)
            # 使用 INTER_LINEAR 兼顾速度和质量
            orig_frame_ui = cv2.resize(
                orig_frame,
                (target_ui_width, target_ui_height),
                interpolation=cv2.INTER_LINEAR,
            )
        else:
            orig_frame_ui = orig_frame

        if len(result.boxes) > 0:
            annotated_frame = result.plot()
            if w > target_ui_width:
                annotated_frame_ui = cv2.resize(
                    annotated_frame,
                    (target_ui_width, target_ui_height),
                    interpolation=cv2.INTER_LINEAR,
                )
            else:
                annotated_frame_ui = annotated_frame
        else:
            annotated_frame_ui = orig_frame_ui

        # 2. 直接使用 QImage.Format_BGR888 避免 cv2.cvtColor 的 CPU 消耗
        def to_qimage(cv_img):
            h, w, ch = cv_img.shape
            bytes_per_line = ch * w
            # 使用 Format_BGR888 直接读取 BGR 数据
            return QImage(
                cv_img.data, w, h, bytes_per_line, QImage.Format_BGR888
            ).copy()

        raw_q_image = to_qimage(orig_frame_ui)

        # 如果没有检测到目标，结果图直接复用原始图的 QImage 引用
        if len(result.boxes) > 0:
            res_q_image = to_qimage(annotated_frame_ui)
        else:
            res_q_image = raw_q_image

        # 3. 提取详细检测信息
        defects = []
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls_id = int(box.cls[0])
            conf_score = float(box.conf[0])
            cls_name = CLASS_NAMES.get(cls_id, f"class_{cls_id}")

            defects.append(
                {
                    "class": cls_name,
                    "class_id": cls_id,
                    "confidence": round(conf_score, 4),
                    "bbox": [x1, y1, x2, y2],
                    "bbox_center": [round((x1 + x2) / 2), round((y1 + y2) / 2)],
                    "bbox_size": [x2 - x1, y2 - y1],
                }
            )

        # 4. 发送信号给主界面
        self.raw_frame_signal.emit(raw_q_image)
        self.frame_signal.emit(res_q_image)
        self.results_signal.emit(defects)

        # 5. 计算并发送统计信息
        num_classes = len(result.boxes.cls.unique())
        num_targets = len(result.boxes)
        # 获取推理速度 (ms) 并转换为 FPS
        speed = result.speed["inference"] + result.speed["postprocess"]
        fps = 1000 / speed if speed > 0 else 0
        self.stats_signal.emit(num_classes, num_targets, fps)

    def stop(self):
        self.is_running = False
        # 清空队列
        while not self.frame_queue.empty():
            try:
                self.frame_queue.get_nowait()
                self.frame_queue.task_done()
            except queue.Empty:
                break
        self.wait()
