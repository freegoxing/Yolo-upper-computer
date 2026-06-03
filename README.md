# YOLO 智能视觉检测上位机系统

> **2026年电子设计大赛“英特尔杯”专题赛作品**
> 
> **参赛单位：南昌大学**
> **参赛队伍：智检微钢队**

本仓库包含了一套基于 **Intel OpenVINO™** 加速引擎和 **PySide6** 框架开发的智能视觉检测上位机系统。系统旨在通过异构计算（CPU + iGPU）实现工业级实时目标检测，并支持与 FPGA 通过千兆以太网（UDP）进行高速原始视频流交互，适配嵌入式边缘计算场景。

---

## 1. 核心特性

*   **硬件加速推理**：集成 Intel OpenVINO™ 工具套件，深度优化 YOLO 模型，充分释放 Intel 处理器集成显卡（iGPU）的推理性能。
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

## 3. 环境准备

### 3.1 硬件要求 (竞赛推荐平台)
*   **开发板**：**DK-2500 系列嵌入式开发板**
*   **处理器**：**Intel® Core™ Ultra 5 Processor 225U** (Arrow Lake 架构)
*   **图形核心**：**Intel® Graphics** (支持 OpenVINO™ 硬件加速推理)
*   **网络接口**：**4 x Intel® i210 GbE LAN** (提供稳定的千兆以太网数据传输，确保 UDP 视频流低延迟重组)

### 3.2 软件安装 (推荐使用 uv)

1. **克隆项目**：
   ```bash
   git clone https://github.com/your-repo/yolo-upper-computer.git
   cd yolo-upper-computer
   ```

2. **安装依赖**：
   ```bash
   uv sync
   ```

3. **OpenVINO 运行时配置 (Linux)**：
   确保系统中已安装 Intel 显卡驱动，以支持 `intel:gpu` 推理。

---

## 4. 快速运行

使用项目根目录的脚本直接启动：
```bash
./run.sh
```
或者手动通过 Python 启动：
```bash
source .venv/bin/activate
python src/main.py
```

---

## 5. FPGA 接入规范

若需使用 FPGA 作为视频源，请参考以下配置：

### 5.1 网络配置
*   **FPGA IP**: `192.168.137.2`
*   **PC IP**: `192.168.137.1` (请手动设置网卡 IPv4 地址)
*   **端口**: `6001` (UDP)

### 5.2 数据包格式 (Header 32 Bytes)
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

详细的 Linux 环境网卡调优方案请参见：`tools/fpga/README.md`。

---

## 6. 模型转换与量化 (OpenVINO)

为了在 Intel iGPU/NPU 上获得最佳推理性能，建议将 PyTorch 的 `.pt` 权重文件转换为 OpenVINO 格式。本系统支持 **FP16** 和 **INT8** 两种精度。

### 6.1 转换操作
在项目环境下运行导出工具：

```bash
# 1. 导出为标准 FP16 格式 (推荐用于 iGPU)
uv run python tools/model_export/export_openvino.py models/best.pt

# 2. 导出为 INT8 量化格式 (极致性能，需校准数据集)
uv run python tools/model_export/export_openvino.py models/best.pt --int8 --data configs/neu_det.yaml
```

### 6.2 关键参数说明
*   **--int8**: 启用 INT8 量化。在 Intel 平台上可进一步提升推理速度并降低功耗。
*   **--data**: 指定数据集配置文件（`.yaml`）。量化过程需要一小部分真实图片（验证集）来计算激活值的分布情况，从而保证量化后的模型精度。
*   **配置目录**: 所有的量化校准配置建议存放在项目根目录的 `configs/` 文件夹下。

详细说明请参考：`tools/model_export/README.md`。

---

## 7. 开发者指南

*   **UI 修改**：编辑 `src/ui/home.ui` (使用 Qt Designer)，运行相关转换脚本更新 `home_ui.py`。
*   **参数配置**：在 `src/config/yolo_config.py` 中修改默认阈值与路径。
*   **工具箱**：
    *   `tools/model_export/`：模型导出与优化工具。
    *   `tools/fpga/`：FPGA 通信调试与环境检测工具。

---

## 8. 许可证

本项目遵循 [MIT License](LICENSE)。

---

**致谢**：感谢电子设计大赛组委会及英特尔提供的高性能嵌入式计算平台支持。
