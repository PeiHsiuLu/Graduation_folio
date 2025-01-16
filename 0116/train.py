import json
import os
import random

def process_json_files():
    """讀取當前目錄下的所有 JSON 檔案，並格式化內容。"""
    current_directory = os.path.dirname(os.path.abspath(__file__))
    cleaned_data = []

    for filename in os.listdir(current_directory):
        if filename.endswith(".json") and filename != "formatted_data.json":
            file_path = os.path.join(current_directory, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    for entry in data:
                        formatted_entry = {
                            "instruction": entry["instruction"],
                            "context": entry["context"].get("content", ""),
                            "response": random.choice(entry["response"]) if entry["response"] else ""
                        }
                        cleaned_data.append(formatted_entry)
                except json.JSONDecodeError:
                    print(f"警告：無法解析 JSON 文件 {filename}")

    # 儲存格式化後的數據
    save_cleaned_data(cleaned_data)

def save_cleaned_data(data):
    """將格式化後的數據存入新的 JSON 檔案。"""
    output_file = "formatted_data.json"
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"格式化後的數據已儲存至 {output_file}")

if __name__ == "__main__":
    process_json_files()
