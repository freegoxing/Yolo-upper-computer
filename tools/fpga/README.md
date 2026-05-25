# Linux 版 FPGA UDP 视频接收上位机

## 1. 文件

```text
fpga_udp_video_receiver_linux.py   主接收程序
udp_linux_probe.py                 UDP 探测程序，先判断有没有收到 FPGA 包
linux_setup_check.sh               网卡配置和检测辅助脚本
README_LINUX.txt                   本说明
```

## 2. 当前 FPGA 参数

```text
FPGA IP：192.168.137.2
FPGA UDP 本地端口：6002
Linux 电脑 IP：192.168.137.1
Linux UDP 接收端口：6001
UDP 包长度：1312 Byte
包头长度：32 Byte
图像数据：1280 Byte
图像格式：1280×720 RGB888
```

## 3. 兼容性分析

### 推荐环境

```text
Ubuntu 20.04 / 22.04 / 24.04
Debian 11 / 12
Linux Mint
国产 Ubuntu/Debian 系发行版
```

要求：

```text
Python >= 3.8
有线网卡支持千兆
可以手动设置 IPv4 地址
可安装 numpy / opencv-python
```

### 桌面 Linux

可以显示 OpenCV 窗口：

```bash
python3 fpga_udp_video_receiver_linux.py --bind-ip 0.0.0.0 --port 6001 --scale 0.5 --iface enp3s0 --preflight
```

### 无桌面 Linux / SSH

用无窗口模式：

```bash
python3 fpga_udp_video_receiver_linux.py --bind-ip 0.0.0.0 --port 6001 --no-window --iface enp3s0 --preflight
```

程序仍会统计丢包并随机保存 10 张图片。

### WSL2

不推荐。WSL2 默认 NAT 网络，FPGA 直连物理网卡的 UDP 包通常不能稳定进入 WSL。建议用 Windows 原生 Python、真实 Ubuntu，或者桥接虚拟机。

### 虚拟机

VMware / VirtualBox 必须使用桥接模式 Bridged Adapter，并桥接到连接 FPGA 的物理有线网卡。不要用 NAT。

## 4. 安装依赖

### 桌面 Ubuntu/Debian

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv ethtool tcpdump
python3 -m pip install --upgrade pip
python3 -m pip install numpy opencv-python
```

如果 OpenCV 提示 `libGL.so.1`：

```bash
sudo apt install libgl1 libglib2.0-0
```

### 无桌面环境

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv ethtool tcpdump
python3 -m pip install numpy opencv-python-headless
```

运行时加：

```bash
--no-window
```

## 5. 选择正确网卡

查看网卡：

```bash
ip -br addr
```

不要只看 UP/DOWN。对两个 en 开头的网卡分别执行：

```bash
sudo ethtool enp3s0
sudo ethtool eno1
```

选择：

```text
Link detected: yes
Speed: 1000Mb/s
```

的那个。

## 6. 设置 Linux 网卡 IP

假设 FPGA 连接的是 `enp3s0`：

```bash
sudo ip addr flush dev enp3s0
sudo ip addr add 192.168.137.1/24 dev enp3s0
sudo ip link set enp3s0 up
```

检查：

```bash
ip addr show enp3s0
```

应看到：

```text
inet 192.168.137.1/24
```

这张有线网卡不要设置网关和 DNS。WiFi 可以继续负责上网。

## 7. 一键辅助检查

```bash
chmod +x linux_setup_check.sh
./linux_setup_check.sh enp3s0 6001
```

## 8. 先用 probe 检查 UDP 是否到达

```bash
python3 udp_linux_probe.py --bind-ip 0.0.0.0 --port 6001
```

正常应看到：

```text
len=1312
magic=0xAA0055FF
width=1280
height=720
```

## 9. 抓包检测

```bash
sudo tcpdump -i enp3s0 -n 'arp or udp port 6001'
```

正常 UDP 包：

```text
192.168.137.2.6002 > 192.168.137.1.6001: UDP, length 1312
```

如果什么都没有，优先查网线、网口灯、FPGA 上电、PHY 复位、I_eth_video_en、DDR/video ready。

如果只有 ARP 没有 UDP，检查 Linux IP 是否是 192.168.137.1，且是否配置在正确网卡。

如果 tcpdump 有 UDP 但 Python 没有，检查端口占用：

```bash
sudo ss -lunp | grep 6001
```

## 10. 丢包与横线判断

程序输出：

```text
[FRAME] pic=101 reason=frame_lag got=2158/2160 missing=2 dup=0
```

含义：

```text
missing=0    当前帧无缺包
missing>0    当前帧存在 UDP 缺包
dup>0        有重复包
```

如果横线出现时 missing 不为 0，基本可以判断和 UDP 丢包有关。

如果 missing 长期为 0 仍有横线，重点检查 FPGA 端 DDR 读写、RGB 顺序、width_convert、跨帧切换、HDMI 输入稳定性。

## 11. 降低 Linux 接收端丢包

临时增大 socket 接收缓冲区：

```bash
sudo sysctl -w net.core.rmem_max=134217728
sudo sysctl -w net.core.rmem_default=134217728
```

然后运行：

```bash
python3 fpga_udp_video_receiver_linux.py --bind-ip 0.0.0.0 --port 6001 --rcvbuf 134217728 --iface enp3s0 --preflight
```

如果仍然缺包很多，就需要在 FPGA 端适当增加 UDP 包间隔。
