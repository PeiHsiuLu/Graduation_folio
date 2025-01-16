import json
import random
import os

def load_json(file_path):
    """從指定文件讀取 JSON"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"檔案 {file_path} 不存在。")
        return []
    except json.JSONDecodeError:
        print(f"檔案 {file_path} 不是有效的 JSON 格式。")
        return []

def filter_and_sample(data, keyword, sample_size):
    """根據指定關鍵字篩選並隨機挑選資料"""
    filtered_data = [entry for entry in data if keyword in entry["instruction"]]
    return random.sample(filtered_data, min(sample_size, len(filtered_data)))

def save_json(data, output_path):
    """儲存資料為 JSON"""
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"隨機挑選的資料已儲存至 {output_path}")

def main():
    input_file = "formatted_data.json"  # 請將此路徑修改為你的 JSON 資料檔案
    output_file = "random_sample.json"

    # 載入資料
    data = load_json(input_file)

    # 隨機挑選資料
    knowledge_data = filter_and_sample(data, "知識喵喵", 10)
    huggy_bear_data = filter_and_sample(data, "抱抱熊", 10)

    # 合併挑選的資料
    sampled_data = knowledge_data + huggy_bear_data

    # 儲存結果
    save_json(sampled_data, output_file)

if __name__ == "__main__":
    main()
