import pandas as pd
import os
import re
import sys

# 配置区：请确保这些路径是正确的
CSV_DIRECTORY = 
OUTPUT_DIRECTORY = CSV_DIRECTORY


def analyze_diagnosis_correctness(df: pd.DataFrame, target_disease: str):
    """
    对传入的DataFrame应用诊断正确性判断逻辑。
    
    新逻辑：
    判断 'All_Diagnoses' 字符串中是否存在【任意一个】诊断名
    包含目标疾病的关键词。
    """
    results = []
    
    # 准备进行不区分大小写的比较
    target_keyword = target_disease.lower()

    for index, row in df.iterrows():
        all_diagnoses_str = row.get('All_Diagnoses', '')

        # 检查 'All_Diagnoses' 单元格是否为有效字符串
        if not isinstance(all_diagnoses_str, str) or not all_diagnoses_str.strip():
            results.append(False)
            continue
            
        # 按 '|' 分割字符串，并获取所有诊断结果
        diagnoses = [d.strip() for d in all_diagnoses_str.split('|')]
        
        # --- 核心改动开始 ---
        # 使用 any() 函数检查列表中是否有任意一个诊断包含目标关键词
        # any() 会遍历所有诊断，只要有一个满足条件 (target_keyword in d.lower())，就会返回 True
        is_correct = any(target_keyword in d.lower() for d in diagnoses)
        results.append(is_correct)
        # --- 核心改动结束 ---
            
    return results


def main(data_path, output_path):
    """
    主函数，执行文件查找、处理、统计和保存。
    （此函数内容无需修改）
    """
    # 检查指定的目录是否存在
    if not os.path.isdir(data_path):
        print(f"错误：指定的CSV目录不存在: {data_path}")
        sys.exit(1)
        
    # 确保输出目录存在
    os.makedirs(output_path, exist_ok=True)

    # 查找所有符合条件的CSV文件
    try:
        files_to_process = [f for f in os.listdir(data_path) if f.endswith('_combined_consistent.csv')]
    except OSError as e:
        print(f"错误：无法访问目录 {data_path}: {e}")
        sys.exit(1)

    if not files_to_process:
        print(f"错误：在目录 '{data_path}' 中未找到任何 `..._combined_consistent.csv` 文件。")
        sys.exit(1)

    print(f"在 '{data_path}' 中找到 {len(files_to_process)} 个待处理的文件...\n")

    overall_correct = 0
    overall_total = 0

    # 遍历并处理每个文件
    for filename in files_to_process:
        # 构建完整的文件路径
        full_file_path = os.path.join(data_path, filename)
        try:
            target_disease = filename.replace('_combined_consistent.csv', '')
            print(f"--- 正在处理文件: {filename} (目标疾病: {target_disease}) ---")
            
            df = pd.read_csv(full_file_path)
            
            # 使用修改后的新逻辑函数
            correctness_column = analyze_diagnosis_correctness(df, target_disease)
            df['is_diagnosis_correct'] = correctness_column
            
            correct_count = df['is_diagnosis_correct'].sum()
            total_count = len(df)
            overall_correct += correct_count
            overall_total += total_count
            
            percentage = (correct_count / total_count * 100) if total_count > 0 else 0
            
            print(f"统计结果: 正确诊断数 {correct_count} / 总病例数 {total_count} ({percentage:.2f}%)")
            
            output_filename = filename.replace('_combined_consistent.csv', '_analysis_results.csv')
            # 构建完整的输出文件路径
            full_output_path = os.path.join(output_path, output_filename)
            df.to_csv(full_output_path, index=False, encoding='utf-8-sig')
            print(f"已保存分析结果到: {full_output_path}\n")

        except FileNotFoundError:
            print(f"错误：文件 {full_file_path} 未找到，已跳过。")
        except Exception as e:
            print(f"处理文件 {filename} 时发生未知错误: {e}")

    print("="*50)
    print("所有文件处理完毕！")
    overall_percentage = (overall_correct / overall_total * 100) if overall_total > 0 else 0
    print(f"总计: 正确诊断数 {overall_correct} / 总病例数 {overall_total} ({overall_percentage:.2f}%)")
    print("="*50)


if __name__ == '__main__':
    # 检查配置的路径是否为空
    if not CSV_DIRECTORY:
        print("错误：请在脚本顶部的配置区设置 'CSV_DIRECTORY' 的路径。")
    else:
        main(CSV_DIRECTORY, OUTPUT_DIRECTORY)