import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current_dir, "ui"))

from config.yolo_config import (
    CONF_THRESHOLD,
    DEFAULT_MODEL_PATH,
    IOU_THRESHOLD,
)
from ui.home_ui import Ui_MainWindow
from utils.udp_thread import UdpReceiverThread
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

        # 2. 缺陷统计 UI 设置
        self.setup_defect_stats()

        # 3. 初始化线程
        self.yolo_thread = YoloThread()
        self.yolo_thread.device = "intel:gpu"
        self.udp_thread = UdpReceiverThread()

        # 连接 YOLO 信号
        self.yolo_thread.raw_frame_signal.connect(self.update_raw_video_label)
        self.yolo_thread.frame_signal.connect(self.update_res_video_label)
        self.yolo_thread.stats_signal.connect(self.update_stats)
        self.yolo_thread.results_signal.connect(self.process_detection_results)

        # 连接 UDP 信号到 YOLO
        self.udp_thread.frame_ready.connect(self.yolo_thread.process_single_frame)

        # 3. 界面交互
        self.init_thresholds()

        # 绑定源切换按钮
        self.src_file_button.clicked.connect(lambda: self.select_source("file"))
        self.src_cam_button.clicked.connect(lambda: self.select_source("camera"))
        self.src_rtsp_button.clicked.connect(lambda: self.select_source("rtsp"))
        self.src_udp_button.clicked.connect(lambda: self.select_source("udp"))

        # 4. 绑定运行按钮
        self.run_button_cam.clicked.connect(self.toggle_inference)

        # 设置默认值
        self.model_path = DEFAULT_MODEL_PATH
        self.current_source_type = "file"  # 默认模式
        self.test_source = "../test/steel.mp4"

    def select_source(self, src_type):
        self.current_source_type = src_type
        if src_type == "file":
            self.status_bar.setText("Source switched to: File")
        elif src_type == "camera":
            self.test_source = 0
            self.status_bar.setText("Source switched to: Camera")
        elif src_type == "rtsp":
            self.test_source = "rtsp://admin:123456@192.168.1.100"
            self.status_bar.setText("Source switched to: RTSP")
        elif src_type == "udp":
            self.status_bar.setText("Source switched to: FPGA UDP (0.0.0.0:6001)")

    def init_thresholds(self):
        # 初始化置信度
        self.conf_spinbox_cam.setValue(CONF_THRESHOLD)
        self.conf_slider_cam.setValue(int(CONF_THRESHOLD * 100))
        # 初始化 IoU
        self.iou_spinbox_cam.setValue(IOU_THRESHOLD)
        self.iou_slider_cam.setValue(int(IOU_THRESHOLD * 100))

        # 信号连接：SpinBox -> Slider
        self.conf_spinbox_cam.valueChanged.connect(
            lambda v: self.conf_slider_cam.setValue(int(v * 100))
        )
        self.iou_spinbox_cam.valueChanged.connect(
            lambda v: self.iou_slider_cam.setValue(int(v * 100))
        )

        # 信号连接：Slider -> SpinBox
        self.conf_slider_cam.valueChanged.connect(
            lambda v: self.conf_spinbox_cam.setValue(v / 100.0)
        )
        self.iou_slider_cam.valueChanged.connect(
            lambda v: self.iou_spinbox_cam.setValue(v / 100.0)
        )

        # 信号连接：更新线程参数
        self.conf_spinbox_cam.valueChanged.connect(self.update_thread_params)
        self.iou_spinbox_cam.valueChanged.connect(self.update_thread_params)

    def update_thread_params(self):
        self.yolo_thread.conf_threshold = self.conf_spinbox_cam.value()
        self.yolo_thread.iou_threshold = self.iou_spinbox_cam.value()

    def setup_defect_stats(self):
        # 映射 UI 文件中定义的 label 到统计字典
        self.defect_widgets = {
            "crazing": self.count_crazing,
            "inclusion": self.count_inclusion,
            "patches": self.count_patches,
            "pitted_surface": self.count_pitted_surface,
            "rolled-in_scale": self.count_rolled_in_scale,
            "scratches": self.count_scratches,
        }

    def process_detection_results(self, defects):
        # 1. 重置各类别计数
        counts = {name: 0 for name in self.defect_widgets.keys()}

        # 2. 累加当前帧检测结果
        for d in defects:
            cls_name = d["class"]
            if cls_name in counts:
                counts[cls_name] += 1

        # 3. 更新 UI 上的数字
        for cls_name, count in counts.items():
            self.defect_widgets[cls_name].setText(str(count))

        # 4. 状态栏处理
        if defects:
            latest = defects[0]
            self.status_bar.setText(
                f"Detected: {latest['class']} ({latest['confidence']:.2f})"
            )
        else:
            self.status_bar.setText("Running... No defects detected.")

    def toggle_inference(self):
        if self.run_button_cam.isChecked():
            # 开始推理
            if self.yolo_thread.load_model(self.model_path):
                self.yolo_thread.is_running = True

                if self.current_source_type == "udp":
                    # UDP 模式：启动 UDP 接收，YOLO 线程只负责处理信号（不进入 run 循环）
                    self.udp_thread.start()
                    self.status_bar.setText("UDP Inference Started...")
                else:
                    # 标准模式：YOLO 线程自带 run 循环
                    self.yolo_thread.source = self.test_source
                    self.yolo_thread.start()
                    self.status_bar.setText(f"Inference Started: {self.test_source}")

                self.run_button_cam.setToolTip("Stop")
        else:
            # 停止推理
            self.yolo_thread.stop()
            if self.udp_thread.isRunning():
                self.udp_thread.stop()
            self.run_button_cam.setToolTip("Start")
            self.status_bar.setText("Inference Stopped.")

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
        self.udp_thread.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Home = MainWindow()
    Home.show()
    sys.exit(app.exec())
