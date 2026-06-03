# OpenVINO 性能基准测试工具

本工具用于测试导出后的 OpenVINO 模型在不同硬件设备（CPU, iGPU, NPU）上的推理性能。

## 1. 使用场景

- **对比精度影响**：对比 FP16 与 INT8 模型在同一硬件上的速度差异。
- **选择推理设备**：测试模型在 `cpu` 和 `intel:gpu` 上的 FPS 表现。
- **性能调优**：观察预处理、推理、后处理各阶段的耗时占比。

## 2. 快速使用

使用 `uv` 运行：

```bash
# 在 Intel 集成显卡上测试默认模型
uv run python tools/benchmark/bench_ov.py --model models/best_openvino_model --device intel:gpu

# 在 CPU 上测试
uv run python tools/benchmark/bench_ov.py --model models/best_openvino_model --device cpu
```

## 3. 参数详解

| 参数 | 默认值 | 描述 |
| :--- | :--- | :--- |
| `--model` | `models/best_openvino_model` | 模型文件夹或 `.xml` 的路径。 |
| `--device` | `intel:gpu` | 推理设备：`cpu`, `intel:gpu`, `npu`。 |
| `--imgsz` | `640` | 推理输入分辨率。 |
| `--rounds` | `50` | 测试轮数，轮数越多结果越平均。 |

## 4. 输出指标说明

- **LATENCY mode**: 侧重于降低单帧延迟，适合对实时性要求极高的上位机显示。
- **THROUGHPUT mode**: 侧重于提升整体吞吐量，适合后台大批量数据处理。
- **Time Breakdown**:
    - **Preprocess**: 图像缩放、颜色空间转换、归一化耗时。
    - **Inference**: 神经网络核心计算耗时。
    - **Postprocess**: NMS（非极大值抑制）及结果解析耗时。

## 5. 注意事项

- **首次运行**：首次加载到 GPU 时可能会有较长的编译时间，属于正常现象。
- **硬件占用**：测试时请关闭其他占用 GPU 的程序以获得最准确的跑分结果。
