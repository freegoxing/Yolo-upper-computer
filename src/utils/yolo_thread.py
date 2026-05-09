import cv2
import numpy as np
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QImage
from ultralytics import YOLO

class YoloThread(QThread):
    # 定义信号：发送原始画面
    raw_frame_signal = Signal(QImage)
    # 定义信号：发送处理后的画面
    frame_signal = Signal(QImage)
    # 定义信号：发送检测到的结果信息 (类别数, 目标总数, FPS)
    stats_signal = Signal(int, int, float)

    def __init__(self):
        super().__init__()
        self.model = None
        self.source = None  # 输入源 (0, 'video.mp4', 'image.jpg')
        self.is_running = True
        self.conf_threshold = 0.25
        self.iou_threshold = 0.45

    def load_model(self, model_path):
        try:
            self.model = YOLO(model_path)
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
            stream=True  # 迭代器模式，节省内存
        )

        for result in results:
            if not self.is_running:
                break

            # 1. 获取原始图片和绘制了检测框的图片 (numpy array)
            orig_frame = result.orig_img
            annotated_frame = result.plot()

            # 2. 转换颜色空间 (BGR -> RGB) 并转换为 QImage
            def to_qimage(cv_img):
                rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb_image.shape
                bytes_per_line = ch * w
                return QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888).copy()

            raw_q_image = to_qimage(orig_frame)
            res_q_image = to_qimage(annotated_frame)

            # 4. 发送信号给主界面显示
            self.raw_frame_signal.emit(raw_q_image)
            self.frame_signal.emit(res_q_image)

            # 5. 计算并发送统计信息
            num_classes = len(result.boxes.cls.unique())
            num_targets = len(result.boxes)
            # 获取推理速度 (ms) 并转换为 FPS
            speed = result.speed['inference']
            fps = 1000 / speed if speed > 0 else 0
            self.stats_signal.emit(num_classes, num_targets, fps)

    def stop(self):
        self.is_running = False
        self.wait()
