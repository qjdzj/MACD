import os 
os.environ["CUDA_VISIBLE_DEVICES"] = "3"

import torch as th
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModel
import numpy as np
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# 加载BioBERT模型和分词器
def load_biobert():
    tokenizer = AutoTokenizer.from_pretrained(
        '/data2/kunzhang/MIMIC-CDM_Models/BioBert'
        )
    model = AutoModel.from_pretrained('/data2/kunzhang/MIMIC-CDM_Models/BioBert')
    return tokenizer, model

# 将文本转化为向量
def encode_texts(texts, tokenizer, model, max_length=128):
    inputs = tokenizer(texts, padding=True, truncation=True, max_length=max_length, return_tensors="pt")
    with th.no_grad():
        outputs = model(**inputs)
    # 使用[CLS]标记的隐藏状态作为文本向量
    return outputs.last_hidden_state[:, 0, :].numpy()

# 计算相似度矩阵
def compute_similarity_matrix(embeddings):
    return cosine_similarity(embeddings)

# 筛选出相似度最低的文本子集
def select_low_similarity_subset(texts, embeddings, num_to_select):
    similarity_matrix = compute_similarity_matrix(embeddings)
    selected_indices = []
    remaining_indices = set(range(len(texts)))

    # 贪心策略：每次选择与当前集合的最大相似度最小的条目
    for _ in range(num_to_select):
        min_sim = float("inf")
        best_idx = None
        for idx in remaining_indices:
            if not selected_indices:
                # 初次选择任意一个
                best_idx = idx
                break
            # 计算该条目与已选集合的最大相似度
            max_sim_to_selected = max(similarity_matrix[idx][i] for i in selected_indices)
            if max_sim_to_selected < min_sim:
                min_sim = max_sim_to_selected
                best_idx = idx

        selected_indices.append(best_idx)
        remaining_indices.remove(best_idx)

    # 返回选定的文本子集
    selected_texts = [texts[i] for i in selected_indices]
    return selected_texts

# 主函数
def main():
    # 示例文本数据
    texts = [
"Ground-glass opacities on radiographs and CT scans",
"Nodular opacities with ground-glass opacity in the superior segment of the right lower lobe",
"Mild diffuse bronchial wall thickening",
"Geographic areas of ground-glass opacity within the left upper lobe",
"Bililateral ill-defined opacities in the lower lungs concerning for multifocal pneumonia",
"Presence of pleuritic chest pain radiating to the back",
"Decreased appetite and weight loss",
"Recent history of hospitalization for PNA and hypoxia",
"Mature arteriovenous fistula",
"Reduced exercise tolerance",
"Presence of leukocytes in urine",
"Heterogeneous ground glass opacifications in both lungs",
"Small bilateral pleural effusions",
"Recent history of stroke",
"History of aspiration",
    ]

    num_to_select = 7  # 需要选择的诊断依据数量

    # 加载模型并向量化
    tokenizer, model = load_biobert()
    embeddings = encode_texts(texts, tokenizer, model)

    # 筛选相似度最低的文本
    selected_texts = select_low_similarity_subset(texts, embeddings, num_to_select)
    print("选定的诊断依据：")
    for text in selected_texts:
        print(text)

# 运行主函数
if __name__ == "__main__":
    main()
