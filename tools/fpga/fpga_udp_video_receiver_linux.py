#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fpga_udp_video_receiver_linux.py

Linux 版 FPGA UDP RGB888 视频接收上位机。
适配包格式：
    UDP datagram : 1312 Byte
    header       : 32 Byte, little-endian 8 x uint32
    image data   : 1280 Byte
包头：
    magic, width, height, total, offset, picseq, framseq, framesize = struct.unpack("<8I", data[:32])
"""

import argparse
import os
import platform
import random
import shutil
import socket
import struct
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    import cv2
except Exception as e:
    print("[ERROR] OpenCV(cv2) 导入失败。")
    print("桌面 Linux：python3 -m pip install numpy opencv-python")
    print("无桌面 Linux：python3 -m pip install numpy opencv-python-headless")
    print("若提示 libGL.so.1 缺失：sudo apt install libgl1 libglib2.0-0")
    print("原始错误：", e)
    sys.exit(1)

try:
    import numpy as np
except Exception as e:
    print("[ERROR] NumPy 导入失败：python3 -m pip install numpy")
    print("原始错误：", e)
    sys.exit(1)

MAGIC = 0xAA0055FF
HEADER_LEN = 32


def run_cmd(cmd: List[str], timeout: float = 3.0) -> Tuple[int, str, str]:
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except FileNotFoundError:
        return 127, "", f"command not found: {cmd[0]}"
    except subprocess.TimeoutExpired:
        return 124, "", f"command timeout: {' '.join(cmd)}"
    except Exception as e:
        return 1, "", str(e)


def read_file(path: str) -> Optional[str]:
    try:
        return Path(path).read_text(encoding="utf-8").strip()
    except Exception:
        return None


def linux_preflight(args) -> None:
    print("\n========== Linux 运行前自检 ==========")
    print(f"Python              : {sys.version.split()[0]}")
    print(f"System              : {platform.platform()}")
    print(f"OpenCV              : {getattr(cv2, '__version__', 'unknown')}")
    print(f"NumPy               : {getattr(np, '__version__', 'unknown')}")
    print(f"DISPLAY             : {os.environ.get('DISPLAY') or '<empty>'}")
    print(f"WAYLAND_DISPLAY     : {os.environ.get('WAYLAND_DISPLAY') or '<empty>'}")

    if not args.no_window and not os.environ.get("DISPLAY") and not os.environ.get("WAYLAND_DISPLAY"):
        print("[WARN] 当前没有图形显示环境，建议使用 --no-window。")

    print("\n[网卡列表：ip -br addr]")
    rc, out, err = run_cmd(["ip", "-br", "addr"])
    print(out if rc == 0 else f"[WARN] {err}")

    if args.iface:
        print(f"\n[指定网卡：{args.iface}]")
        rc, out, err = run_cmd(["ip", "addr", "show", args.iface])
        print(out if rc == 0 else f"[WARN] {err}")

        operstate = read_file(f"/sys/class/net/{args.iface}/operstate")
        carrier = read_file(f"/sys/class/net/{args.iface}/carrier")
        speed = read_file(f"/sys/class/net/{args.iface}/speed")
        print(f"operstate           : {operstate or '<unknown>'}")
        print(f"carrier             : {carrier or '<unknown>'}")
        print(f"speed               : {(speed + ' Mb/s') if speed and speed != '-1' else '<unknown>'}")

        if carrier == "0":
            print("[WARN] carrier=0，物理链路没有起来。检查网线、FPGA 上电、网口灯、PHY 复位。")
        if speed and speed not in ("-1", "1000"):
            print("[WARN] 当前不是千兆链路。视频 UDP 高速传输建议 1000Mb/s。")

        if shutil.which("ethtool"):
            rc, out, err = run_cmd(["ethtool", args.iface])
            print("\n[ethtool]")
            print(out if out else err)
        else:
            print("[INFO] 没有 ethtool，可安装：sudo apt install ethtool")

    print("\n[端口占用检查]")
    if shutil.which("ss"):
        rc, out, err = run_cmd(["ss", "-lunp"])
        if rc == 0:
            hit = [line for line in out.splitlines() if f":{args.port}" in line]
            print("\n".join(hit) if hit else f"UDP {args.port} 端口未发现占用。")
            if hit:
                print("[WARN] 如果这不是当前程序，可能导致 bind 失败。")
        else:
            print(f"[WARN] ss 查询失败：{err}")
    else:
        print("[INFO] 没有 ss 命令，跳过。")

    print("\n[Linux UDP 接收缓冲区限制]")
    for key in ("rmem_default", "rmem_max"):
        val = read_file(f"/proc/sys/net/core/{key}")
        print(f"net.core.{key:<12}: {val or '<unknown>'}")
    try:
        rmem_max = int(read_file("/proc/sys/net/core/rmem_max") or "0")
        if rmem_max and rmem_max < args.rcvbuf:
            print("[WARN] rmem_max 小于程序请求的 --rcvbuf，实际缓冲区可能被限制。")
            print("可临时增大：")
            print("sudo sysctl -w net.core.rmem_max=134217728")
            print("sudo sysctl -w net.core.rmem_default=134217728")
    except ValueError:
        pass

    print("\n[推荐 FPGA 直连配置]")
    if args.iface:
        print(f"sudo ip addr flush dev {args.iface}")
        print(f"sudo ip addr add 192.168.137.1/24 dev {args.iface}")
        print(f"sudo ip link set {args.iface} up")
        print(f"sudo tcpdump -i {args.iface} -n 'arp or udp port {args.port}'")
    else:
        print("先用 ip -br addr 找连接 FPGA 的网卡，例如 enp3s0，然后：")
        print("sudo ip addr flush dev enp3s0")
        print("sudo ip addr add 192.168.137.1/24 dev enp3s0")
        print("sudo ip link set enp3s0 up")
        print(f"sudo tcpdump -i enp3s0 -n 'arp or udp port {args.port}'")
    print("=====================================\n")


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

    def __post_init__(self) -> None:
        if not self.received:
            self.received = bytearray(self.expected_packets)

    @property
    def expected_packets(self) -> int:
        return (self.total + self.packet_payload_size - 1) // self.packet_payload_size

    @property
    def missing_packets(self) -> int:
        return self.expected_packets - self.got_packets

    @property
    def is_complete(self) -> bool:
        return self.got_packets >= self.expected_packets

    def add_packet(self, offset: int, payload: bytes) -> bool:
        self.last_time = time.time()

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

        self.buf[offset:end] = payload[:end - offset]
        self.received[pkt_idx] = 1
        self.got_packets += 1
        return True


class UdpVideoReceiverLinux:
    def __init__(self, args):
        self.args = args

        if not args.no_window and not os.environ.get("DISPLAY") and not os.environ.get("WAYLAND_DISPLAY"):
            print("[WARN] 没有检测到 DISPLAY/WAYLAND_DISPLAY，自动切换为 --no-window。")
            self.args.no_window = True

        self.frames: Dict[int, FrameState] = {}
        self.latest_picseq: Optional[int] = None
        self.last_good_frame_bytes: Optional[bytes] = None

        self.total_udp_packets = 0
        self.total_video_packets = 0
        self.total_bad_magic = 0
        self.total_bad_len = 0
        self.total_bad_dim = 0
        self.total_bad_offset = 0
        self.total_duplicate = 0

        self.output_frames = 0
        self.complete_frames = 0
        self.incomplete_frames = 0
        self.total_expected_packets = 0
        self.total_missing_packets = 0
        self.start_time = time.time()

        self.saved_count = 0
        self.save_dir = Path(args.save_dir)
        self.save_dir.mkdir(parents=True, exist_ok=True)
        self.next_save_gap = random.randint(args.random_min_gap, args.random_max_gap)
        self.last_display_bgr: Optional[np.ndarray] = None

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        if args.bind_device:
            if not args.iface:
                print("[WARN] --bind-device 需要同时指定 --iface，已忽略。")
            else:
                try:
                    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, args.iface.encode() + b"\0")
                    print(f"[INFO] Socket 已绑定到网卡：{args.iface}")
                except PermissionError:
                    print("[WARN] SO_BINDTODEVICE 权限不足。可用 sudo 运行，或去掉 --bind-device。")
                except Exception as e:
                    print(f"[WARN] SO_BINDTODEVICE 失败：{e}")

        try:
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, args.rcvbuf)
        except Exception as e:
            print(f"[WARN] 设置 SO_RCVBUF 失败：{e}")

        self.sock.bind((args.bind_ip, args.port))
        self.sock.settimeout(args.socket_timeout)

        actual_buf = self.sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
        print(f"[INFO] Listening on {args.bind_ip}:{args.port}")
        print(f"[INFO] SO_RCVBUF requested={args.rcvbuf}, actual={actual_buf}")
        print(f"[INFO] Save dir: {self.save_dir.resolve()}")
        print("[INFO] q 退出，s 手动保存当前帧。" if not args.no_window else "[INFO] --no-window 模式，Ctrl+C 退出。")

    def make_initial_buffer(self, total: int) -> bytearray:
        if self.args.conceal_missing and self.last_good_frame_bytes is not None and len(self.last_good_frame_bytes) == total:
            return bytearray(self.last_good_frame_bytes)
        return bytearray(total)

    def parse_packet(self, data: bytes):
        self.total_udp_packets += 1

        if len(data) < HEADER_LEN:
            self.total_bad_len += 1
            return None

        try:
            magic, width, height, total, offset, picseq, framseq, framesize = struct.unpack("<8I", data[:HEADER_LEN])
        except struct.error:
            self.total_bad_len += 1
            return None

        if magic != MAGIC:
            self.total_bad_magic += 1
            return None

        payload = data[HEADER_LEN:]

        if self.args.expected_datagram > 0 and len(data) != self.args.expected_datagram:
            self.total_bad_len += 1
            if self.args.drop_unexpected_datagram:
                return None

        if self.args.strict_packet_len and len(payload) != framesize:
            self.total_bad_len += 1
            return None

        if width <= 0 or height <= 0 or total <= 0 or framesize <= 0:
            self.total_bad_dim += 1
            return None

        expected_total = width * height * self.args.channels
        if self.args.strict_dim and total != expected_total:
            self.total_bad_dim += 1
            return None

        if offset >= total or offset + len(payload) > total + framesize:
            self.total_bad_offset += 1
            return None

        return width, height, total, offset, picseq, framseq, framesize, payload

    def get_frame(self, picseq: int, width: int, height: int, total: int, framesize: int) -> FrameState:
        if picseq not in self.frames:
            self.frames[picseq] = FrameState(
                picseq=picseq,
                width=width,
                height=height,
                channels=self.args.channels,
                total=total,
                packet_payload_size=framesize,
                buf=self.make_initial_buffer(total),
            )
        if self.latest_picseq is None or picseq > self.latest_picseq:
            self.latest_picseq = picseq
        return self.frames[picseq]

    def finish_frame(self, picseq: int, reason: str) -> None:
        frame = self.frames.pop(picseq, None)
        if frame is None:
            return

        self.output_frames += 1
        if frame.is_complete:
            self.complete_frames += 1
        else:
            self.incomplete_frames += 1

        self.total_expected_packets += frame.expected_packets
        self.total_missing_packets += frame.missing_packets
        self.total_duplicate += frame.duplicate_packets
        self.total_bad_offset += frame.bad_offset_packets

        try:
            arr_rgb = np.frombuffer(frame.buf, dtype=np.uint8).reshape((frame.height, frame.width, frame.channels))
        except ValueError:
            print(f"[WARN] frame reshape failed: pic={frame.picseq}, total={frame.total}")
            return

        if self.args.rgb_order == "RGB":
            arr_bgr = cv2.cvtColor(arr_rgb, cv2.COLOR_RGB2BGR)
        else:
            arr_bgr = arr_rgb

        self.last_display_bgr = arr_bgr

        if frame.is_complete or self.args.use_incomplete_as_reference:
            self.last_good_frame_bytes = bytes(frame.buf)

        self.maybe_save_random(arr_bgr, frame)

        if not self.args.no_window:
            show = arr_bgr
            if self.args.scale != 1.0:
                show = cv2.resize(arr_bgr, None, fx=self.args.scale, fy=self.args.scale, interpolation=cv2.INTER_AREA)
            if self.args.overlay:
                self.draw_overlay(show, frame, reason)
            cv2.imshow(self.args.window_name, show)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                raise KeyboardInterrupt
            if key == ord("s"):
                self.save_frame(arr_bgr, frame, manual=True)

        self.print_frame_stats(frame, reason)

    def draw_overlay(self, img, frame: FrameState, reason: str) -> None:
        elapsed = max(time.time() - self.start_time, 1e-6)
        fps = self.output_frames / elapsed
        loss = self.loss_rate()
        lines = [
            f"pic={frame.picseq} {frame.width}x{frame.height} fps={fps:.1f} reason={reason}",
            f"frame missing={frame.missing_packets}/{frame.expected_packets}, dup={frame.duplicate_packets}",
            f"total missing={self.total_missing_packets}, loss={loss:.4f}%, saved={self.saved_count}/{self.args.save_random}",
        ]
        x, y = 20, 30
        for i, line in enumerate(lines):
            cv2.putText(img, line, (x, y + 28 * i), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 255, 0), 2, cv2.LINE_AA)

    def maybe_save_random(self, img_bgr, frame: FrameState) -> None:
        if self.args.save_random <= 0 or self.saved_count >= self.args.save_random:
            return
        if frame.missing_packets > self.args.max_save_missing:
            return
        self.next_save_gap -= 1
        if self.next_save_gap > 0:
            return
        self.save_frame(img_bgr, frame, manual=False)
        self.saved_count += 1
        self.next_save_gap = random.randint(self.args.random_min_gap, self.args.random_max_gap)

    def save_frame(self, img_bgr, frame: FrameState, manual: bool = False) -> None:
        tag = "manual" if manual else "random"
        ts = time.strftime("%Y%m%d_%H%M%S")
        name = f"{tag}_pic{frame.picseq}_missing{frame.missing_packets}_dup{frame.duplicate_packets}_{ts}_{int(time.time()*1000)%1000:03d}.png"
        path = self.save_dir / name
        ok = cv2.imwrite(str(path), img_bgr)
        print(f"[SAVE] {path.resolve()}" if ok else f"[WARN] failed to save: {path}")

    def loss_rate(self) -> float:
        if self.total_expected_packets <= 0:
            return 0.0
        return self.total_missing_packets / self.total_expected_packets * 100.0

    def print_frame_stats(self, frame: FrameState, reason: str) -> None:
        if self.args.print_every <= 0:
            return
        if (self.output_frames % self.args.print_every != 0 and
                frame.missing_packets == 0 and frame.duplicate_packets == 0 and reason == "complete"):
            return
        elapsed = max(time.time() - self.start_time, 1e-6)
        fps = self.output_frames / elapsed
        print(
            f"[FRAME] pic={frame.picseq} reason={reason} "
            f"got={frame.got_packets}/{frame.expected_packets} "
            f"missing={frame.missing_packets} dup={frame.duplicate_packets} "
            f"complete={self.complete_frames} incomplete={self.incomplete_frames} "
            f"fps={fps:.2f} total_loss={self.loss_rate():.5f}% "
            f"bad_len={self.total_bad_len} bad_magic={self.total_bad_magic} bad_offset={self.total_bad_offset}"
        )

    def flush_old_frames(self) -> None:
        if not self.frames:
            return

        now = time.time()
        timeout_pics = [
            pic for pic, st in self.frames.items()
            if now - st.last_time >= self.args.frame_timeout
        ]
        for pic in sorted(timeout_pics):
            self.finish_frame(pic, "timeout")

        if not self.frames or self.latest_picseq is None:
            return

        while len(self.frames) > self.args.max_active_frames:
            self.finish_frame(min(self.frames.keys()), "buffer_limit")

        lag_pics = [pic for pic in self.frames if self.latest_picseq - pic > self.args.max_frame_lag]
        for pic in sorted(lag_pics):
            self.finish_frame(pic, "frame_lag")

    def run(self) -> None:
        try:
            while True:
                try:
                    data, _addr = self.sock.recvfrom(self.args.max_datagram)
                except socket.timeout:
                    self.flush_old_frames()
                    continue

                parsed = self.parse_packet(data)
                if parsed is None:
                    continue

                width, height, total, offset, picseq, _framseq, framesize, payload = parsed
                frame = self.get_frame(picseq, width, height, total, framesize)
                if frame.add_packet(offset, payload):
                    self.total_video_packets += 1

                if frame.is_complete:
                    self.finish_frame(picseq, "complete")

                self.flush_old_frames()

        except KeyboardInterrupt:
            print("\n[INFO] stopping...")
        finally:
            for pic in sorted(list(self.frames.keys())):
                self.finish_frame(pic, "exit")
            if not self.args.no_window:
                try:
                    cv2.destroyAllWindows()
                except Exception:
                    pass
            self.print_summary()

    def print_summary(self) -> None:
        elapsed = max(time.time() - self.start_time, 1e-6)
        print("\n========== UDP VIDEO RECEIVER SUMMARY ==========")
        print(f"Elapsed time             : {elapsed:.2f} s")
        print(f"Output frames            : {self.output_frames}")
        print(f"Complete frames          : {self.complete_frames}")
        print(f"Incomplete frames        : {self.incomplete_frames}")
        print(f"Average output FPS       : {self.output_frames / elapsed:.2f}")
        print(f"Total UDP datagrams      : {self.total_udp_packets}")
        print(f"Valid video packets      : {self.total_video_packets}")
        print(f"Expected video packets   : {self.total_expected_packets}")
        print(f"Missing video packets    : {self.total_missing_packets}")
        print(f"Packet loss rate         : {self.loss_rate():.6f}%")
        print(f"Duplicate packets        : {self.total_duplicate}")
        print(f"Bad length packets       : {self.total_bad_len}")
        print(f"Bad magic packets        : {self.total_bad_magic}")
        print(f"Bad dimension packets    : {self.total_bad_dim}")
        print(f"Bad offset packets       : {self.total_bad_offset}")
        print(f"Random saved images      : {self.saved_count}/{self.args.save_random}")
        print(f"Save directory           : {self.save_dir.resolve()}")
        print("===============================================")


def build_arg_parser():
    p = argparse.ArgumentParser(description="Linux FPGA UDP RGB888 video receiver")
    p.add_argument("--bind-ip", default="0.0.0.0", help="本地绑定 IP，第一次建议 0.0.0.0。")
    p.add_argument("--port", type=int, default=6001, help="Linux UDP 接收端口，默认 6001。")
    p.add_argument("--iface", default="", help="连接 FPGA 的网卡名，例如 enp3s0/eno1/eth0。")
    p.add_argument("--bind-device", action="store_true", help="强制 socket 绑定到 --iface，通常需要 sudo。")
    p.add_argument("--preflight", action="store_true", help="运行前打印 Linux 网络和环境自检。")
    p.add_argument("--channels", type=int, default=3, help="RGB888 = 3。")
    p.add_argument("--scale", type=float, default=0.5, help="显示缩放比例。")
    p.add_argument("--window-name", default="FPGA UDP Video", help="OpenCV 窗口名。")
    p.add_argument("--no-window", action="store_true", help="无窗口模式，适合 SSH/无桌面。")
    p.add_argument("--overlay", action="store_true", default=True, help="窗口叠加统计信息。")
    p.add_argument("--no-overlay", dest="overlay", action="store_false", help="关闭窗口叠加统计。")
    p.add_argument("--rgb-order", default="RGB", choices=["RGB", "BGR"], help="颜色顺序，红蓝反了试 BGR。")
    p.add_argument("--rcvbuf", type=int, default=64 * 1024 * 1024, help="UDP 接收缓冲区。")
    p.add_argument("--max-datagram", type=int, default=4096, help="recvfrom 最大长度。")
    p.add_argument("--socket-timeout", type=float, default=0.01, help="socket 超时秒数。")
    p.add_argument("--expected-datagram", type=int, default=1312, help="期望 UDP 包长度，设 0 不检查。")
    p.add_argument("--drop-unexpected-datagram", action="store_true", help="长度不符时丢包。")
    p.add_argument("--frame-timeout", type=float, default=0.20, help="单帧等待超时。")
    p.add_argument("--max-frame-lag", type=int, default=1, help="允许跨帧乱序的滞后帧数。")
    p.add_argument("--max-active-frames", type=int, default=3, help="最大活动帧缓存。")
    p.add_argument("--strict-packet-len", action="store_true", help="要求 payload 长度等于 IMG_FRAMSIZE。")
    p.add_argument("--strict-dim", action="store_true", help="要求 IMG_TOTAL=width*height*channels。")
    p.add_argument("--conceal-missing", action="store_true", default=True, help="用上一帧补偿缺包位置。")
    p.add_argument("--no-conceal-missing", dest="conceal_missing", action="store_false", help="关闭缺包补偿。")
    p.add_argument("--use-incomplete-as-reference", action="store_true", help="允许不完整帧作为补偿参考。")
    p.add_argument("--print-every", type=int, default=30, help="每 N 帧打印统计；异常帧会立即打印。")
    p.add_argument("--save-random", type=int, default=10, help="随机保存 N 张图片。")
    p.add_argument("--save-dir", default="saved_random_frames_linux", help="保存目录。")
    p.add_argument("--random-min-gap", type=int, default=5, help="随机保存最小帧间隔。")
    p.add_argument("--random-max-gap", type=int, default=60, help="随机保存最大帧间隔。")
    p.add_argument("--max-save-missing", type=int, default=999999, help="只保存缺包数 <= 该值的帧；0 表示只保存完整帧。")
    return p


def main() -> None:
    args = build_arg_parser().parse_args()
    if args.random_min_gap <= 0:
        args.random_min_gap = 1
    if args.random_max_gap < args.random_min_gap:
        args.random_max_gap = args.random_min_gap
    if args.preflight:
        linux_preflight(args)
    receiver = UdpVideoReceiverLinux(args)
    receiver.run()


if __name__ == "__main__":
    main()
