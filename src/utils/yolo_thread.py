import cv2
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
        self.device = 'intel:gpu'  # 默认设备

    def load_model(self, model_path):
        try:
            self.model = YOLO(model_path, task='detect')
            return True
        except Exception as e:
            print(f"Error loading model: {e}")
            return False

    def run(self):
        if self.model is None or self.source is None:
            return

        # 使用 ultralytics 的 stream 模式
        results = self.model.predict(
            source=self.source,
            conf=self.conf_threshold,
            iou=self.iou_threshold,
            stream=True,
            device=self.device,
            half=True,  # 开启半精度 (FP16)，Intel GPU 提速明显
        )

        for result in results:
            if not self.is_running:
                break

            # 1. 获取原始图片和绘制了检测框的图片 (numpy array)
            orig_frame = result.orig_img
            
            # 如果没有检测到目标，直接使用原图，避免 result.plot() 的额外耗时
            if len(result.boxes) > 0:
                annotated_frame = result.plot()
            else:
                annotated_frame = orig_frame

            # 2. 直接使用 QImage.Format_BGR888 避免 cv2.cvtColor 的 CPU 消耗
            def to_qimage(cv_img):
                h, w, ch = cv_img.shape
                bytes_per_line = ch * w
                # 使用 Format_BGR888 直接读取 BGR 数据，减少转换开销
                return QImage(
                    cv_img.data, w, h, bytes_per_line, QImage.Format_BGR888
                ).copy()

            raw_q_image = to_qimage(orig_frame)
            
            # 如果没有检测到目标，结果图直接复用原始图的 QImage 引用
            if len(result.boxes) > 0:
                res_q_image = to_qimage(annotated_frame)
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
            speed = result.speed["inference"]
            fps = 1000 / speed if speed > 0 else 0
            self.stats_signal.emit(num_classes, num_targets, fps)

    def stop(self):
        self.is_running = False
        self.wait()
