import argparse
import os
import time

import numpy as np
from ultralytics import YOLO


def benchmark(model_path, device="intel:gpu", imgsz=640, rounds=50):
    """
    OpenVINO 模型性能基准测试工具
    :param model_path: 模型文件夹或 .xml 路径
    :param device: 推理设备 (cpu, intel:gpu, npx)
    :param imgsz: 输入图像大小
    :param rounds: 测试轮数
    """
    print(f"Loading model: {model_path} on {device}...")
    # task="detect" 明确指定为检测任务
    model = YOLO(model_path, task="detect")

    # 创建模拟帧 (1920x1080)
    frame = np.zeros((1080, 1920, 3), dtype=np.uint8)

    print("Warming up (热身中)...")
    for _ in range(5):
        model.predict(
            source=frame, device=device, imgsz=imgsz, half=True, verbose=False
        )

    print(f"Starting benchmark for {rounds} rounds...")
    latencies = []
    pre_times = []
    inf_times = []
    post_times = []

    # --- 测试延时模式 (LATENCY) ---
    for i in range(rounds):
        start = time.perf_counter()
        results = model.predict(
            source=frame,
            device=device,
            imgsz=imgsz,
            half=True,
            verbose=False,
            ov_config={"PERFORMANCE_HINT": "LATENCY"},
        )
        end = time.perf_counter()

        latencies.append((end - start) * 1000)
        res = results[0]
        pre_times.append(res.speed["preprocess"])
        inf_times.append(res.speed["inference"])
        post_times.append(res.speed["postprocess"])

    print("\nResults (LATENCY mode - 专注实时性):")
    print(
        f"  Total Wall Clock: {np.mean(latencies):.2f} ms ({1000 / np.mean(latencies):.2f} FPS)"
    )
    print(f"  Preprocess:       {np.mean(pre_times):.2f} ms")
    print(f"  Inference:        {np.mean(inf_times):.2f} ms")
    print(f"  Postprocess:      {np.mean(post_times):.2f} ms")

    # --- 测试吞吐量模式 (THROUGHPUT) ---
    print("\nTesting THROUGHPUT mode (专注吞吐量)...")
    latencies_tp = []
    for i in range(rounds):
        start = time.perf_counter()
        results = model.predict(
            source=frame,
            device=device,
            imgsz=imgsz,
            half=True,
            verbose=False,
            ov_config={"PERFORMANCE_HINT": "THROUGHPUT"},
        )
        end = time.perf_counter()
        latencies_tp.append((end - start) * 1000)

    print("Results (THROUGHPUT mode):")
    print(
        f"  Total Wall Clock: {np.mean(latencies_tp):.2f} ms ({1000 / np.mean(latencies_tp):.2f} FPS)"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OpenVINO 模型性能测试工具")
    parser.add_argument(
        "--model", type=str, default="models/best_openvino_model", help="模型路径"
    )
    parser.add_argument(
        "--device", type=str, default="intel:gpu", help="推理设备 (cpu, intel:gpu)"
    )
    parser.add_argument("--imgsz", type=int, default=640, help="输入分辨率")
    parser.add_argument("--rounds", type=int, default=50, help="测试轮数")

    args = parser.parse_args()

    if os.path.exists(args.model):
        benchmark(args.model, args.device, args.imgsz, args.rounds)
    else:
        print(f"错误: 找不到模型路径 {args.model}")
