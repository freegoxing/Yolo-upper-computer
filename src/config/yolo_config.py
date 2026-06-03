import os

# 项目根目录 (Yolo-upper-computer/)
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

# ==================== 模型配置 ====================
# 默认模型路径
DEFAULT_MODEL_PATH = os.path.join(ROOT_DIR, "models", "best_openvino_model")

# 数据集配置路径 (用于 INT8 量化和模型导出)
DATA_CONFIG_PATH = os.path.join(ROOT_DIR, "configs", "neu_det.yaml")

# 类别名称（针对 NEU-DET 6类数据）
# 注意：此处的定义应与 configs/neu_det.yaml 中的 names 保持一致
CLASS_NAMES = {
    0: "crazing",          # 龟裂
    1: "inclusion",        # 夹杂物
    2: "patches",          # 斑块
    3: "pitted_surface",   # 点蚀面
    4: "rolled-in_scale",  # 压入氧化铁皮
    5: "scratches",        # 划痕
}

# ==================== 默认检测参数 ====================
CONF_THRESHOLD = 0.25
IOU_THRESHOLD = 0.45

# ==================== 导出配置 ====================
# 默认是否导出为 INT8 (若为 False 则默认导出 FP16)
DEFAULT_EXPORT_INT8 = True
