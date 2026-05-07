import os
import sys
import time
import json
import threading
import traceback
from pathlib import Path
from collections import defaultdict

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMenu, QVBoxLayout
from PySide6.QtGui import QImage, QPixmap, QColor
from PySide6.QtCore import QTimer, QThread, Signal, QObject, QPoint, Qt

current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(current_dir, "ui"))

from ui.home import Ui_MainWindow
from utils.ui_functions import UIFunctions


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 1. 解决最大化不缩放的问题：
        # 我们手动给 MainWidget 添加一个布局，把 Main_QF 放进去，使其随窗口缩放。
        self.central_layout = QVBoxLayout(self.MainWidget)
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_layout.addWidget(self.Main_QF)

        # 2. 窗口设置
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground) 
        
        UIFunctions.uiDefinitions(self)

    def mousePressEvent(self, event):
        # 3. 使用新 API globalPosition() 消除警告
        self.dragPos = event.globalPosition().toPoint()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    Home = MainWindow()
    Home.show()
    # 4. 使用 exec() 代替 exec_()
    sys.exit(app.exec())
