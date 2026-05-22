import os

# ==================== 模型配置 ====================
# 默认模型路径
DEFAULT_MODEL_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..","models", "best_openvino_model"
)

# 类别名称（针对 NEU-DET 6类数据）
CLASS_NAMES = {
    0: "crazing",  # 龟裂
    1: "inclusion",  # 夹杂物
    2: "patches",  # 斑块
    3: "pitted_surface",  # 点蚀面
    4: "rolled-in_scale",  # 压入氧化铁皮
    5: "scratches",  # 划痕
}

# 默认检测参数
CONF_THRESHOLD = 0.25
IOU_THRESHOLD = 0.45
