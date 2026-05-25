#!/usr/bin/env bash
set -e

IFACE="${1:-}"
PORT="${2:-6001}"

if [ -z "$IFACE" ]; then
  echo "用法：./linux_setup_check.sh <网卡名> [端口]"
  echo "例如：./linux_setup_check.sh enp3s0 6001"
  echo "先查看网卡：ip -br addr"
  exit 1
fi

echo "========== FPGA UDP Linux Setup Check =========="
echo "[1] 当前网卡信息"
ip -br addr || true

echo
echo "[2] 配置 FPGA 直连网卡 IP：192.168.137.1/24"
sudo ip addr flush dev "$IFACE"
sudo ip addr add 192.168.137.1/24 dev "$IFACE"
sudo ip link set "$IFACE" up

echo
echo "[3] 设置后的网卡状态"
ip addr show "$IFACE"

echo
echo "[4] 链路状态"
if command -v ethtool >/dev/null 2>&1; then
  sudo ethtool "$IFACE" || true
else
  echo "未安装 ethtool，可执行：sudo apt install ethtool"
fi

echo
echo "[5] UDP socket 缓冲区"
echo "当前 rmem_max: $(cat /proc/sys/net/core/rmem_max 2>/dev/null || echo unknown)"
echo "丢包严重时可临时执行："
echo "sudo sysctl -w net.core.rmem_max=134217728"
echo "sudo sysctl -w net.core.rmem_default=134217728"

echo
echo "[6] 抓包命令"
echo "sudo tcpdump -i $IFACE -n 'arp or udp port $PORT'"

echo
echo "[7] 探测命令"
echo "python3 udp_linux_probe.py --bind-ip 0.0.0.0 --port $PORT"

echo
echo "[8] 视频接收命令"
echo "python3 fpga_udp_video_receiver_linux.py --bind-ip 0.0.0.0 --port $PORT --scale 0.5 --iface $IFACE --preflight"
echo "================================================"
