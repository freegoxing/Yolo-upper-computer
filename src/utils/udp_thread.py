import socket
import struct
import time
from dataclasses import dataclass, field
from typing import Dict, Optional, Tuple

import cv2
import numpy as np
from PySide6.QtCore import QThread, Signal

MAGIC = 0xAA0055FF
HEADER_LEN = 32


@dataclass
class FrameState:
    picseq: int
    width: int
    height: int
    channels: int
    total: int
    packet_payload_size: int
    buf: bytearray
    first_time: float = field(default_factory=time.time)
    last_time: float = field(default_factory=time.time)
    received: bytearray = field(default_factory=bytearray)
    got_packets: int = 0
    duplicate_packets: int = 0
    bad_offset_packets: int = 0

    def __post_init__(self):
        expected = self.expected_packets
        if not self.received:
            self.received = bytearray(expected)

    @property
    def expected_packets(self) -> int:
        return (self.total + self.packet_payload_size - 1) // self.packet_payload_size

    @property
    def is_complete(self) -> bool:
        return self.got_packets >= self.expected_packets

    def add_packet(self, offset: int, payload: bytes) -> bool:
        if offset < 0 or offset >= self.total:
            self.bad_offset_packets += 1
            return False
        end = min(offset + len(payload), self.total)
        if end <= offset:
            self.bad_offset_packets += 1
            return False
        pkt_idx = offset // self.packet_payload_size
        if pkt_idx < 0 or pkt_idx >= self.expected_packets:
            self.bad_offset_packets += 1
            return False
        if self.received[pkt_idx]:
            self.duplicate_packets += 1
            return False
        self.buf[offset:end] = payload[: end - offset]
        self.received[pkt_idx] = 1
        self.got_packets += 1
        return True


class UdpReceiverThread(QThread):
    frame_ready = Signal(np.ndarray)

    def __init__(self, bind_ip="0.0.0.0", port=6001):
        super().__init__()
        self.bind_ip = bind_ip
        self.port = port
        self.is_running = False
        
        # Default settings from the stable script
        self.channels = 3
        self.rcvbuf = 64 * 1024 * 1024
        self.max_datagram = 4096
        self.socket_timeout = 0.01
        self.frame_timeout = 0.20
        self.max_frame_lag = 1
        self.max_active_frames = 3
        self.conceal_missing = True
        self.rgb_order = "RGB"

        self.frames: Dict[int, FrameState] = {}
        self.latest_picseq: Optional[int] = None
        self.last_good_frame_bytes: Optional[bytes] = None
        self.sock = None

    def stop(self):
        self.is_running = False
        self.wait()

    def make_initial_buffer(self, total: int) -> bytearray:
        if self.conceal_missing and self.last_good_frame_bytes is not None and len(self.last_good_frame_bytes) == total:
            return bytearray(self.last_good_frame_bytes)
        return bytearray(total)

    def parse_packet(self, data: bytes) -> Optional[Tuple[int, int, int, int, int, int, int, int, bytes]]:
        if len(data) < HEADER_LEN:
            return None
        try:
            magic, width, height, total, offset, picseq, framseq, framesize = struct.unpack("<8I", data[:HEADER_LEN])
        except struct.error:
            return None
        if magic != MAGIC:
            return None
        payload = data[HEADER_LEN:]
        if width <= 0 or height <= 0 or total <= 0 or framesize <= 0:
            return None
        return magic, width, height, total, offset, picseq, framseq, framesize, payload

    def get_or_create_frame(self, picseq: int, width: int, height: int, total: int, framesize: int) -> FrameState:
        if picseq not in self.frames:
            self.frames[picseq] = FrameState(
                picseq=picseq,
                width=width,
                height=height,
                channels=self.channels,
                total=total,
                packet_payload_size=framesize,
                buf=self.make_initial_buffer(total),
            )
        if self.latest_picseq is None or picseq > self.latest_picseq:
            self.latest_picseq = picseq
        return self.frames[picseq]

    def finish_frame(self, picseq: int):
        frame = self.frames.pop(picseq, None)
        if frame is None:
            return
        try:
            arr_rgb = np.frombuffer(frame.buf, dtype=np.uint8).reshape((frame.height, frame.width, frame.channels))
            if self.rgb_order.upper() == "RGB":
                arr_bgr = cv2.cvtColor(arr_rgb, cv2.COLOR_RGB2BGR)
            else:
                arr_bgr = arr_rgb
            
            if frame.is_complete:
                self.last_good_frame_bytes = bytes(frame.buf)
            
            self.frame_ready.emit(arr_bgr)
        except Exception as e:
            print(f"Frame reassembly error: {e}")

    def flush_old_frames(self):
        if not self.frames:
            return
        now = time.time()
        old_by_timeout = [pic for pic, st in self.frames.items() if now - st.last_time >= self.frame_timeout]
        for pic in sorted(old_by_timeout):
            self.finish_frame(pic)
        if not self.frames or self.latest_picseq is None:
            return
        while len(self.frames) > self.max_active_frames:
            oldest = min(self.frames.keys())
            self.finish_frame(oldest)
        old_by_lag = [pic for pic in self.frames.keys() if self.latest_picseq - pic > self.max_frame_lag]
        for pic in sorted(old_by_lag):
            self.finish_frame(pic)

    def run(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, self.rcvbuf)
        try:
            self.sock.bind((self.bind_ip, self.port))
        except Exception as e:
            print(f"Socket bind failed: {e}")
            return
        self.sock.settimeout(self.socket_timeout)
        self.is_running = True

        while self.is_running:
            try:
                data, addr = self.sock.recvfrom(self.max_datagram)
                parsed = self.parse_packet(data)
                if parsed:
                    _, width, height, total, offset, picseq, _, framesize, payload = parsed
                    frame = self.get_or_create_frame(picseq, width, height, total, framesize)
                    frame.add_packet(offset, payload)
                    if frame.is_complete:
                        self.finish_frame(picseq)
                self.flush_old_frames()
            except socket.timeout:
                self.flush_old_frames()
                continue
            except Exception as e:
                if self.is_running:
                    print(f"UDP Recv Error: {e}")
                break
        
        if self.sock:
            self.sock.close()
            self.sock = None
