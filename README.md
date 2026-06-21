# YOLO 智能视觉检测上位机系统

> **2026年电子设计大赛“英特尔杯”专题赛作品**
> 
> **参赛单位：南昌大学**
> **参赛队伍：智检微钢队**

本仓库包含了一套基于 **Intel OpenVINO™** 加速引擎和 **PySide6** 框架开发的智能视觉检测上位机系统。系统旨在通过异构计算（CPU + iGPU）实现工业级实时目标检测，并支持与 FPGA 通过千兆以太网（UDP）进行高速原始视频流交互，适配嵌入式边缘计算场景。

---

## 1. 核心特性

*   **硬件加速推理**：集成 Intel OpenVINO™ 工具套件，深度优化 YOLO 模型，充分释放 Intel 处理器集成显卡（GPU）的推理性能。
*   **高速异构协同**：专为 FPGA 实时视频传输设计的 UDP 接收协议，支持 1280×720 RGB888 原始流接收，具备乱序重组、丢包补偿与接收缓冲区自动调优能力。
*   **全场景源支持**：
    *   **FPGA 流**：对接千兆网原始 UDP 视频流。
    *   **网络流**：支持标准 RTSP/RTMP 协议。
    *   **本地硬件**：支持 USB 摄像头及工业相机。
    *   **离线分析**：支持主流视频文件格式。
*   **高性能并发架构**：
    *   **UI 线程**：基于 PySide6 打造的高实时性无边框响应界面。
    *   **推理线程**：独立的 YOLO 推理循环，支持模型热加载与参数实时调节。
    *   **采集线程**：零拷贝思想的 UDP 数据包重组逻辑，确保高帧率下 CPU 占用率处于低位。
*   **📈 可视化监控**：实时呈现 FPS、目标计数、类别分布及置信度统计，支持原始画面与推理结果画面的双通道对比显示。

---

## 2. 技术架构

### 2.1 软件栈
*   **开发语言**：Python 3.13+
*   **UI 框架**：PySide6 (Qt for Python 6.8+)
*   **推理引擎**：Ultralytics YOLO + OpenVINO™
*   **图像处理**：OpenCV-Python-Headless
*   **依赖管理**：[uv](https://github.com/astral-sh/uv) (高速 Python 依赖打包工具)

### 2.2 系统拓扑
```text
[ FPGA / Camera ] --- (UDP/CSI/USB) ---> [ Intel Upper Computer ]
                                                |
                                        [ OpenVINO Inference ]
                                                |
                                        [ PySide6 UI Display ]
```

---

## 3. 项目目录结构

```text
.
├── assets/                 # Qt 资源文件与界面图标
│   └── img/                # 按钮、状态、参数等 UI 图标素材
├── configs/                # 数据集、量化、校准等 YAML 配置
├── models/                 # 本地模型权重与导出的 OpenVINO 模型目录
├── src/                    # 上位机主程序源码
│   ├── main.py             # PySide6 GUI 程序入口
│   ├── config/             # 运行时默认参数与模型/推理配置
│   ├── models/             # 应用侧模型相关代码或预留扩展目录
│   ├── ui/                 # Qt Designer UI、资源编译产物与界面模块
│   └── utils/              # 推理、视频采集、UDP 接收、UI 辅助线程
├── tools/                  # 离线工具、诊断脚本与性能测试脚本
│   ├── benchmark/          # OpenVINO 推理性能基准测试
│   ├── fpga/               # FPGA UDP 视频流接收、探测与 Linux 网卡检查
│   └── model_export/       # YOLO 权重导出为 OpenVINO/INT8 模型
├── run.sh                  # 启动脚本，支持 GUI 启动与 FPGA 网卡初始化
├── pyproject.toml          # Python 项目元数据、依赖与 Ruff 配置
└── uv.lock                 # uv 依赖锁文件
```

### 3.1 核心源码说明

*   `src/main.py`：应用启动入口，负责创建 Qt 应用、加载主窗口并启动整体 GUI 流程。
*   `src/config/yolo_config.py`：集中维护模型路径、推理阈值、输入源、设备选择等默认配置。
*   `src/utils/yolo_thread.py`：YOLO/OpenVINO 推理线程，处理模型加载、推理循环与检测结果输出。
*   `src/utils/video_thread.py`：普通视频源读取线程，支持UDP输入。
*   `src/utils/udp_thread.py`：FPGA UDP 原始视频流接收与帧重组线程。
*   `src/utils/ui_functions.py`：主界面交互、控件状态、窗口行为等 UI 辅助逻辑。
*   `src/ui/home.ui`：Qt Designer 原始界面文件，界面布局修改应优先编辑该文件。
*   `src/ui/home_ui.py`：由 `home.ui` 生成的 Python UI 文件，通常不手动修改。
*   `src/ui/resources_rc.py`：由 Qt 资源文件生成的资源模块，通常不手动修改。

### 3.2 工具与资源说明

*   `assets/resources.qrc`：Qt 资源索引文件，用于将 `assets/img/` 中的图标打包给界面使用。
*   `configs/neu_det.yaml`：模型量化/校准时使用的数据集配置示例。
*   `tools/model_export/export_openvino.py`：将 Ultralytics YOLO `.pt` 权重导出为 OpenVINO 模型，支持 FP16 与 INT8。
*   `tools/benchmark/bench_ov.py`：OpenVINO 模型推理性能测试脚本。
*   `tools/fpga/udp_linux_probe.py`：Linux 下 UDP 收包与链路探测工具。
*   `tools/fpga/linux_setup_check.sh`：Linux 网卡、缓冲区与系统参数检查脚本。
*   `tools/fpga/fpga_udp_video_receiver_linux.py`：FPGA UDP 原始视频流接收验证脚本。

---

## 4. 环境准备

### 4.1 硬件要求 (竞赛推荐平台)
*   **开发板**：**DK-2500 系列嵌入式开发板**
*   **处理器**：**Intel® Core™ Ultra 5 Processor 225U** (Arrow Lake 架构)
*   **图形核心**：**Intel® Graphics** (支持 OpenVINO™ 硬件加速推理)
*   **网络接口**：**4 x Intel® i210 GbE LAN** (提供稳定的千兆以太网数据传输，确保 UDP 视频流低延迟重组)

### 4.2 软件安装 (推荐使用 uv)

1. **克隆项目**：
   ```bash
   git clone https://github.com/freegoxing/Yolo-upper-computer.git
   cd yolo-upper-computer
   ```

2. **安装依赖**：
   ```bash
   uv sync
   ```

3. **OpenVINO 运行时配置 (Linux)**：
   确保系统中已安装 Intel 显卡驱动，以支持 `intel:gpu` 推理。

---

## 5. 快速运行

使用项目根目录的脚本直接启动：
```bash
./run.sh
```

如果需要在启动前自动配置连接 FPGA 的有线网口，可通过 `--setup`
指定网口名称：

```bash
./run.sh --setup enp3s0
```

该命令会将指定网口配置为 `192.168.137.1/24`，拉起网口，并设置
Linux UDP 接收缓冲区：
```bash
sudo ip addr flush dev enp3s0
sudo ip addr add 192.168.137.1/24 dev enp3s0
sudo ip link set enp3s0 up
sudo sysctl -w net.core.rmem_max=134217728
sudo sysctl -w net.core.rmem_default=134217728
```

或者手动通过 Python 启动：
```bash
source .venv/bin/activate
python src/main.py
```

---

## 6. FPGA 接入规范

若需使用 FPGA 作为视频源，请参考以下配置：

### 6.1 网络配置

*   **FPGA IP**: `192.168.137.2`
*   **PC IP**: `192.168.137.1` (请手动设置网卡 IPv4 地址)
*   **端口**: `6001` (UDP)

Linux 下可直接使用启动脚本配置连接 FPGA 的网口：
```bash
# 查看网卡名称
ip -br addr

# 将指定网口配置为 192.168.137.1/24 并启动上位机
./run.sh --setup <interface>
```

例如 FPGA 接在 `enp3s0`：
```bash
./run.sh --setup enp3s0
```

注意：`--setup` 会清空该网口已有 IP 地址，请确认传入的是连接 FPGA 的有线网口，不要传入正在用于上网或远程连接的网口。

### 6.2 数据包格式 (Header 32 Bytes)
| 偏移量 | 长度 | 描述 |
| :--- | :--- | :--- |
| 0x00 | 4B | Magic Number (`0xAA0055FF`) |
| 0x04 | 4B | 图像宽度 (Default: 1280) |
| 0x08 | 4B | 图像高度 (Default: 720) |
| 0x0C | 4B | 单帧总字节数 |
| 0x10 | 4B | 当前包偏移地址 |
| 0x14 | 4B | 图片序列号 (PicSeq) |
| 0x18 | 4B | 帧内包序号 |
| 0x1C | 4B | 单个包 Payload 长度 (1280B) |

详细的 Linux 环境网卡调优方案请参见：[README](tools/fpga/README.md)。

---

## 7. 模型转换与量化 (OpenVINO)

为了在 Intel iGPU/NPU 上获得最佳推理性能，建议将 PyTorch 的 `.pt` 权重文件转换为 OpenVINO 格式。本系统支持 **FP16** 和 **INT8** 两种精度。

### 7.1 转换操作
在项目环境下运行导出工具：

```bash
# 1. 导出为标准 FP16 格式 (推荐用于 iGPU)
uv run python tools/model_export/export_openvino.py models/best.pt

# 2. 导出为 INT8 量化格式 (极致性能，需校准数据集)
uv run python tools/model_export/export_openvino.py models/best.pt --int8 --data configs/neu_det.yaml
```

### 7.2 关键参数说明
*   **--int8**: 启用 INT8 量化。在 Intel 平台上可进一步提升推理速度并降低功耗。
*   **--data**: 指定数据集配置文件（`.yaml`）。量化过程需要一小部分真实图片（验证集）来计算激活值的分布情况，从而保证量化后的模型精度。
*   **配置目录**: 所有的量化校准配置建议存放在项目根目录的 `configs/` 文件夹下。

详细说明请参考：[README](tools/model_export/README.md)。

---

## 8. 开发者指南

*   **UI 修改**：编辑 `src/ui/home.ui` (使用 Qt Designer)，运行相关转换脚本更新 `home_ui.py`。
*   **参数配置**：在 `src/config/yolo_config.py` 中修改默认阈值与路径。
*   **工具箱**：
    *   `tools/model_export/`：模型导出与优化工具。
    *   `tools/fpga/`：FPGA 通信调试与环境检测工具。

---

## 9. 许可证

本项目遵循 [MIT License](LICENSE)。

---

**致谢**：感谢电子设计大赛组委会及英特尔提供的高性能嵌入式计算平台支持。
