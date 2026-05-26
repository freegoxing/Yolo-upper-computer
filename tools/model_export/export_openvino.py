import argparse

from ultralytics import YOLO


def export_to_openvino(weights_path):
    """
    将 YOLO .pt 权重文件转换为 OpenVINO 格式 (FP16)
    """
    try:
        # 加载模型
        model = YOLO(weights_path)

        # 导出为 OpenVINO 格式
        # half=True 导出为 FP16 格式，适合在 Intel GPU/NPU 上运行
        print(f"正在转换 {weights_path} 为 OpenVINO 格式...")
        export_path = model.export(format="openvino", half=True)

        print("\n转换成功！OpenVINO 模型文件夹已生成。")
        print(f"路径: {export_path}")
    except Exception as e:
        print(f"转换失败: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLO .pt to OpenVINO 转换工具")
    parser.add_argument("weights", type=str, help="输入的 .pt 权重文件路径")

    args = parser.parse_args()
    export_to_openvino(args.weights)
