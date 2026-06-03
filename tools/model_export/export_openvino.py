import argparse

from ultralytics import YOLO


def export_to_openvino(weights_path, int8=False, data=None):
    """
    将 YOLO .pt 权重文件转换为 OpenVINO 格式
    :param weights_path: .pt 文件路径
    :param int8: 是否启用 INT8 量化
    :param data: 用于 INT8 量化的校验数据集 (.yaml 文件)
    """
    try:
        # 加载模型
        model = YOLO(weights_path)

        # 导出为 OpenVINO 格式
        # half=True 导出为 FP16 格式，适合在 Intel GPU/NPU 上运行
        # int8=True 导出为 INT8 格式，需要提供 data 参数进行校准
        print(f"正在转换 {weights_path} 为 OpenVINO 格式 (INT8={int8})...")

        export_args = {
            "format": "openvino",
            "half": not int8,  # 如果不是 INT8，则默认导出 FP16
            "int8": int8,
        }
        if int8 and data:
            export_args["data"] = data
        elif int8 and not data:
            print(
                "警告: 启用 INT8 量化建议提供 --data 参数用于校准，否则将使用模型默认数据集或 coco8.yaml"
            )

        export_path = model.export(**export_args)

        print("\n转换成功！OpenVINO 模型文件夹已生成。")
        print(f"路径: {export_path}")
    except Exception as e:
        print(f"转换失败: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="YOLO .pt to OpenVINO 转换工具")
    parser.add_argument("weights", type=str, help="输入的 .pt 权重文件路径")
    parser.add_argument("--int8", action="store_true", help="是否启用 INT8 量化")
    parser.add_argument(
        "--data", type=str, help="用于 INT8 量化的校验数据集 (.yaml)，如 coco8.yaml"
    )

    args = parser.parse_args()
    export_to_openvino(args.weights, int8=args.int8, data=args.data)
