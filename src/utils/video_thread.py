import cv2
import time
from PySide6.QtCore import QThread, Signal
import numpy as np

class VideoReaderThread(QThread):
    """
    专门负责视频解码的线程 (Producer)
    """
    frame_ready = Signal(np.ndarray)
    finished_signal = Signal()

    def __init__(self, source):
        super().__init__()
        self.source = source
        self.is_running = True

    def run(self):
        cap = cv2.VideoCapture(self.source)
        if not cap.isOpened():
            print(f"Error: Could not open video source {self.source}")
            return

        # 获取视频原始帧率，尝试匹配播放速度
        fps = cap.get(cv2.CAP_PROP_FPS)
        if fps <= 0: fps = 25
        frame_time = 1.0 / fps

        while self.is_running:
            start_time = time.time()
            ret, frame = cap.read()
            if not ret:
                break
            
            self.frame_ready.emit(frame)
            
            # 控制读取速度，防止过快占用过多内存
            # 如果是实时流（如摄像头），cv2 已经处理了速度，文件则需要手动控制
            if isinstance(self.source, str) and not self.source.startswith("rtsp"):
                elapsed = time.time() - start_time
                wait_time = max(0, frame_time - elapsed)
                if wait_time > 0:
                    time.sleep(wait_time)

        cap.release()
        self.finished_signal.emit()

    def stop(self):
        self.is_running = False
        self.wait()
