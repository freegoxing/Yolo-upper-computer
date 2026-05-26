#!/usr/bin/env python3
"""
udp_linux_probe.py
先用它判断 Linux 是否能收到 FPGA 发来的 UDP 包。
"""

import argparse
import socket
import struct
import time

MAGIC = 0xAA0055FF


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--bind-ip", default="0.0.0.0")
    p.add_argument("--port", type=int, default=6001)
    p.add_argument("--count", type=int, default=20)
    p.add_argument("--timeout", type=float, default=3.0)
    p.add_argument("--rcvbuf", type=int, default=16 * 1024 * 1024)
    args = p.parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, args.rcvbuf)
    sock.bind((args.bind_ip, args.port))
    sock.settimeout(args.timeout)

    print(f"[INFO] Listening on {args.bind_ip}:{args.port}")
    print("[INFO] Waiting for FPGA UDP packets...")

    n = 0
    t0 = time.time()
    while n < args.count:
        try:
            data, addr = sock.recvfrom(4096)
        except TimeoutError:
            print(f"[TIMEOUT] {args.timeout}s 内没有收到 UDP 包。")
            print("建议执行：sudo tcpdump -i 你的网卡名 -n 'arp or udp port 6001'")
            continue

        n += 1
        if len(data) >= 32:
            magic, width, height, total, offset, picseq, framseq, framesize = (
                struct.unpack("<8I", data[:32])
            )
            print(
                f"#{n:03d} from={addr} len={len(data)} "
                f"magic=0x{magic:08X} width={width} height={height} total={total} "
                f"offset={offset} picseq={picseq} framseq={framseq} framesize={framesize}"
            )
            if magic != MAGIC:
                print("      [WARN] magic 不等于 0xAA0055FF，可能不是视频 UDP 包。")
        else:
            print(f"#{n:03d} from={addr} len={len(data)} too short")

    elapsed = max(time.time() - t0, 1e-6)
    print(f"[DONE] received={n}, avg_rate={n / elapsed:.1f} packets/s")


if __name__ == "__main__":
    main()
