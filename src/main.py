import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current_dir, "ui"))

from ui.home_ui import Ui_MainWindow
from utils.ui_functions import UIFunctions
from utils.yolo_thread import YoloThread


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # 1. UI 基础设置
        self.central_layout = QVBoxLayout(self.MainWidget)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.addWidget(self.Main_QF)
        self.setWindowFlag(Qt.FramelessWindowHint)
        UIFunctions.uiDefinitions(self)

        # 2. 初始化 YOLO 线程
        self.yolo_thread = YoloThread()
        # 连接信号
        self.yolo_thread.raw_frame_signal.connect(self.update_raw_video_label)
        self.yolo_thread.frame_signal.connect(self.update_res_video_label)
        self.yolo_thread.stats_signal.connect(self.update_stats)

        # 3. 绑定按钮：点击运行按钮开始测试
        self.run_button_cam.clicked.connect(self.toggle_inference)

        # 设置默认模型路径
        self.model_path = "../models/yolov8n.pt"
        # 默认测试图片源 (你可以改成 0 测试摄像头)
        self.test_source = "../test/test.mp4"

    def toggle_inference(self):
        if self.run_button_cam.isChecked():
            # 开始推理
            if self.yolo_thread.load_model(self.model_path):
                self.yolo_thread.source = self.test_source
                self.yolo_thread.is_running = True
                self.yolo_thread.start()
                self.run_button_cam.setToolTip("Stop")
        else:
            # 停止推理
            self.yolo_thread.stop()
            self.run_button_cam.setToolTip("Start")

    def update_raw_video_label(self, q_image):
        self.display_image(q_image, self.pre_cam)

    def update_res_video_label(self, q_image):
        self.display_image(q_image, self.res_cam)

    def display_image(self, q_image, label):
        # 将 QImage 缩放到 label 的大小并显示
        pixmap = QPixmap.fromImage(q_image)
        scaled_pixmap = pixmap.scaled(label.size())
        label.setPixmap(scaled_pixmap)

    def update_stats(self, classes, targets, fps):
        # 更新界面上的数据卡片
        self.Class_num_cam.setText(str(classes))
        self.Target_num_cam.setText(str(targets))
        self.fps_label_cam.setText(f"{fps:.1f}")

    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()

    def closeEvent(self, event):
        # 确保窗口关闭时线程也停止
        self.yolo_thread.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Home = MainWindow()
    Home.show()
    sys.exit(app.exec())
