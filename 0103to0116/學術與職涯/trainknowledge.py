import json
import os
import argparse

def load_json_files():
    """讀取當前目錄下的所有 JSON 檔案並合併數據"""
    merged_data = []
    current_directory = os.path.dirname(os.path.abspath(__file__))
    for filename in os.listdir(current_directory):
        if filename.endswith(".json") and filename != "cleaned_data.json":
            file_path = os.path.join(current_directory, filename)
            with open(file_path, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)
                    formatted_data = convert_to_standard_format(data)
                    merged_data.extend(formatted_data)
                except json.JSONDecodeError:
                    print(f"警告：無法解析 JSON 文件 {file_path}")
    return merged_data

def convert_to_standard_format(data):
    """將 JSON 內容轉換為標準格式"""
    formatted_data = []
    for entry in data:
        formatted_entry = {
            "instruction": "你是一位學識淵博且嚴謹的學術研究員『知識喵喵』，請根據以下內容提供邏輯嚴密且深入的分析，並用簡明易懂的方式解釋。",
            "context": {
                "title": entry.get("title", "無標題"),
                "tags": entry.get("tags", []),
                "content": entry.get("content", "")
            },
            "response": entry.get("comments", [])
        }
        formatted_data.append(formatted_entry)
    return formatted_data

def clean_data(data):
    """清理數據，刪除不符合條件的項目"""
    cleaned_data = []
    seen_entries = set()
    
    for entry in data:
        context = entry.get("context", {})
        title = context.get("title", "").strip()
        content = context.get("content", "").strip()
        tags = tuple(sorted(context.get("tags", [])))
        
        # 唯一識別鍵
        entry_key = (title, content, tags)
        if entry_key in seen_entries:
            continue
        seen_entries.add(entry_key)
        
        # 確保 response 存在且不包含 "通報 📢"
        response = entry.get("response", [])
        if not response or any("通報 📢" in resp for resp in response):
            continue
        
        cleaned_data.append(entry)
    
    return cleaned_data

def save_json(data, output_path):
    """將清理後的數據儲存為 JSON"""
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    print(f"清理後的數據已儲存至 {output_path}")

def main():
    parser = argparse.ArgumentParser(description="訓練數據清理腳本")
    parser.add_argument("-o", "--output", default="cleaned_knowledge.json", help="輸出 JSON 文件名稱")
    
    args = parser.parse_args()
    
    raw_data = load_json_files()
    cleaned_data = clean_data(raw_data)
    save_json(cleaned_data, args.output)

if __name__ == "__main__":
    main()