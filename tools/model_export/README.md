# OpenVINO 模型导出与量化工具

本工具用于将 YOLO 的 PyTorch 权重文件 (`.pt`) 转换为针对 Intel 硬件优化的 **OpenVINO™** 格式。

## 1. 核心功能

- **FP16 导出**：默认精度，适合在 Intel GPU (iGPU) 上运行，在精度和速度之间有极佳平衡。
- **INT8 量化**：极致性能优化，通过校准（Calibration）将模型压缩，适合在 CPU 或支持的加速器上运行。

## 2. 快速使用

使用 `uv` 运行脚本（推荐）：

### 导出 FP16 (推荐)
```bash
uv run python tools/model_export/export_openvino.py path/to/best.pt
```

### 导出 INT8 量化
```bash
uv run python tools/model_export/export_openvino.py path/to/best.pt --int8 --data configs/neu_det.yaml
```

## 3. 参数详解

| 参数 | 必填 | 描述 |
| :--- | :--- | :--- |
| `weights` | 是 | 输入的 `.pt` 权重文件路径。 |
| `--int8` | 否 | 开启后启用 INT8 量化，否则默认为 FP16。 |
| `--data` | 否 | **INT8 量化必备**。指定数据集配置文件 (`.yaml`)。用于校准模型，确保量化精度。 |

## 4. 关于 INT8 量化校准

### 为什么需要 `--data`？
INT8 量化会将 32 位浮点数转换为 8 位整数。为了尽可能减少精度损失，转换工具需要使用一部分真实的图像数据（通常是验证集）来统计模型每一层激活值的动态范围。

### 数据集配置文件 (`.yaml`)
数据集配置文件应存放在项目根目录的 `configs/` 目录下。例如 `configs/neu_det.yaml`，其内容应包含：
- `path`: 数据集根目录。
- `val`: 用于校准/验证的图片路径。
- `names`: 类别名称映射。

## 5. 常见问题

- **精度下降过多**：确保量化时提供的 `--data` 配置中的 `val` 路径下有足够且真实的图片样本。
- **缺少 NNCF**：INT8 量化依赖于 `nncf` 库。如果报错，请运行 `uv add nncf` 安装。
- **导出失败**：请检查 `ultralytics` 版本是否为最新，建议使用项目配套的 `pyproject.toml` 环境。

## 6. 输出结果

脚本运行成功后，会在 `.pt` 文件同级目录下生成一个文件夹（例如 `best_openvino_model/`），其中包含：
- `best.xml`: 网络结构描述。
- `best.bin`: 权重数据。
- `metadata.yaml`: 包含类别名称、预处理参数等模型元数据。

在上位机系统中加载模型时，请直接选择该文件夹。
