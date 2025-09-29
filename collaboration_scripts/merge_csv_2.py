import pandas as pd
import os
import sys
from collections import defaultdict

# --- 配置区 ---
# 1. 设置包含 "round" 文件夹的基础目录路径 (也是我们希望的输出目录)
base_path = 

# 2. 将输出路径设置为与基础路径相同
output_path = base_path
# --- 配置结束 ---

def merge_by_disease(base_path, output_path):
    """
    按疾病名称对CSV文件进行分组和合并，并将结果保存在指定的输出路径中。

    新逻辑:
    - 扫描 'round1', 'round2', 'round3' 文件夹。
    - 对于 'round1' 和 'round2' 中的文件，只提取 'Status' 为 '✅ 一致' 的行。
    - 对于 'round3' 中的文件，提取所有行。
    - 将所有提取的数据按疾病名称合并，并为每种疾病生成一个独立的输出CSV文件。
    """
    data_by_disease = defaultdict(list)

    print(f"开始扫描目录: {base_path}")

    if not os.path.isdir(base_path):
        print(f"错误：输入目录 '{base_path}' 不存在或不是一个目录。请检查路径是否正确。")
        sys.exit(1)

    os.makedirs(output_path, exist_ok=True)
    print(f"文件将被保存到: {output_path}")

    for round_folder in sorted(os.listdir(base_path)):
        round_path = os.path.join(base_path, round_folder)
        
        # 只处理名为 round1, round2, round3 的目录
        if os.path.isdir(round_path) and round_folder in ['round1', 'round2', 'round3']:
            print(f"正在处理文件夹: {round_folder}")
            
            for filename in sorted(os.listdir(round_path)):
                if filename.endswith('.csv'):
                    try:
                        disease_name = filename.split('_')[0]
                    except IndexError:
                        print(f"  - 警告: 无法从 {filename} 中提取疾病名称，已跳过。")
                        continue

                    file_path = os.path.join(round_path, filename)
                    try:
                        df = pd.read_csv(file_path, encoding='utf-8')
                        
                        # --- 核心逻辑修改开始 ---
                        data_to_add = None
                        
                        # 规则1: 对于 round1 和 round2，只提取一致的结果
                        if round_folder in ['round1', 'round2']:
                            if 'Status' in df.columns:
                                data_to_add = df[df['Status'] == '✅ 一致'].copy()
                                print(f"  - 在 {filename} 中根据 [一致] 规则找到 {len(data_to_add)} 行")
                            else:
                                print(f"  - 警告: 在 {filename} 中未找到 'Status' 列，已跳过。")
                        
                        # 规则2: 对于 round3，提取所有结果
                        elif round_folder == 'round3':
                            data_to_add = df.copy()
                            print(f"  - 在 {filename} 中根据 [全部提取] 规则找到 {len(data_to_add)} 行")
                        
                        # 将提取到的数据添加到对应疾病的列表中
                        if data_to_add is not None and not data_to_add.empty:
                            data_by_disease[disease_name].append(data_to_add)
                        # --- 核心逻辑修改结束 ---

                    except Exception as e:
                        print(f"  - 错误: 处理文件 {filename} 时发生错误: {e}")

    if not data_by_disease:
        print("\n处理完成，但未找到任何可供合并的数据。")
        return

    print("\n-------------------------------------------")
    print("所有文件扫描完毕，开始合并和保存...")

    for disease_name, dfs_list in data_by_disease.items():
        if not dfs_list:
            continue

        combined_df = pd.concat(dfs_list, ignore_index=True)
        
        # 注意：这里输出的文件名可以根据需要调整，目前保持不变
        output_filename = f"{disease_name}_combined_consistent.csv"
        full_output_path = os.path.join(output_path, output_filename)

        try:
            combined_df.to_csv(full_output_path, index=False, encoding='utf-8-sig')
            print(f"✅ 成功: '{disease_name}' 的 {len(combined_df)} 行数据已保存到 '{full_output_path}'")
        except Exception as e:
            print(f"❌ 失败: 保存 '{disease_name}' 的数据到 '{full_output_path}' 时发生错误: {e}")
            
    print("-------------------------------------------\n")
    print("🎉 所有任务已完成！")

if __name__ == '__main__':
    if not base_path or not output_path:
        print("错误：脚本顶部的 'base_path' 和 'output_path' 变量不能为空。")
    else:
        merge_by_disease(base_path, output_path)