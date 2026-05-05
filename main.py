from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMenu
from PySide6.QtGui import QImage, QPixmap, QColor
from PySide6.QtCore import QTimer, QThread, Signal, QObject, QPoint, Qt
from ui.home import Ui_MainWindow

from collections import defaultdict
from pathlib import Path

import threading
import traceback
import time
import json
import sys
import os

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.setWindowFlag(Qt.FramelessWindowHint)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    Home = MainWindow()
    Home.show()
    sys.exit(app.exec_())
