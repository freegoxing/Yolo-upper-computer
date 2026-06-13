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
    p.add_argument("--iface", default="", help="可选：网卡名，例如 enx00e04c5e3060。")
    p.add_argument(
        "--bind-device",
        action="store_true",
        help="可选：使用 SO_BINDTODEVICE 绑定到 --iface，需要 sudo 或 CAP_NET_RAW。",
    )
    args = p.parse_args()

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    if args.bind_device:
        if not args.iface:
            print("[WARN] --bind-device 需要同时指定 --iface，已忽略。")
        else:
            try:
                sock.setsockopt(
                    socket.SOL_SOCKET,
                    socket.SO_BINDTODEVICE,
                    args.iface.encode() + b"\0",
                )
                print(f"[INFO] Socket 已绑定到网卡：{args.iface}")
            except PermissionError:
                print("[WARN] SO_BINDTODEVICE 权限不足。请用 sudo 运行，或去掉 --bind-device。")
            except Exception as e:
                print(f"[WARN] SO_BINDTODEVICE 失败：{e}")

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, args.rcvbuf)
    sock.bind((args.bind_ip, args.port))
    sock.settimeout(args.timeout)

    actual_buf = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
    print(f"[INFO] Listening on {args.bind_ip}:{args.port}")
    print(f"[INFO] SO_RCVBUF requested={args.rcvbuf}, actual={actual_buf}")
    print("[INFO] Waiting for FPGA UDP packets...")

    n = 0
    t0 = time.time()
    while n < args.count:
        try:
            data, addr = sock.recvfrom(4096)
        except TimeoutError:
            print(f"[TIMEOUT] {args.timeout}s 内没有收到 UDP 包。")
            print(f"建议执行：sudo tcpdump -i 你的网卡名 -n 'arp or udp port {args.port}'")
            print(
                "如果 tcpdump 能看到 UDP 但这里收不到，请检查：\n"
                "  1) ip addr show 你的网卡名 里是否有 192.168.137.1/24\n"
                f"  2) sudo ss -lunp | grep ':{args.port}' 是否有其他程序占用端口\n"
                "  3) sudo nft list ruleset 或 sudo iptables -S 是否丢弃 UDP\n"
                "  4) sysctl net.ipv4.conf.all.rp_filter net.ipv4.conf.你的网卡名.rp_filter"
            )
            continue
        except KeyboardInterrupt:
            print("\n[INFO] 用户中断。")
            break

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
