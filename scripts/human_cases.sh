MODELS=(
    "Llama3Instruct8B"
    "Llama3Instruct70B"
    "Deepseek-Llama70B-distill"
)

# 在这里添加你要使用的所有随机种子
SEEDS=(1 397 783 1024 1565 2025 2699 3298 4848 5866)

# 7种疾病列表
PATHOLOGIES=(
    "pulmonary embolism"
    "pneumonia"
    "pericarditis"
    "pancreatitis"
    "appendicitis"
    "cholecystitis"
    "diverticulitis"
)

# 指定使用的GPU
GPU_ID=2

# --- 自动化执行区 ---

# 记录开始时间
start_time=$(date +%s)

# 三层嵌套循环，遍历所有组合
for model_name in "${MODELS[@]}"; do
    for seed in "${SEEDS[@]}"; do
        for pathology in "${PATHOLOGIES[@]}"; do
            # 使用 model=$model_name 来让 Hydra 加载对应的配置组
            CUDA_VISIBLE_DEVICES=$GPU_ID python infer.py \
                model="$model_name" \
                pathology="$pathology" \
                seed="$seed" \
                guideline=1
        done
    done
done
