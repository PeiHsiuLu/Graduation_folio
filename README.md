# Graduation_folio
115科技系畢業專題 - 個人紀錄  
[小組畢業專題的紀錄](https://github.com/nrps9909/TAHRD-Graduation-Project)  

# 2024/12/27 進度紀錄
[20241227爬蟲程式碼](https://github.com/PeiHsiuLu/Graduation_folio/tree/main/1227_crawler_record)  
folder 內的程式碼：  
- main.py: 爬蟲程式碼，主要是利用 selenium 進行爬蟲，抓取 Dcard 感情版上的文章內容、留言
- slected_data.json: 測試爬蟲抓取的 200 筆數據資料。
  - title: 文章標題
  - link: 文章連結
  - content: 文章內容
  - comment: 文章留言
  
目前已經確定可以成功爬取 Dcard 上的文章，但是程式碼還必須儲存資料的編號、Dcard 文章的 tag，以方便日後進行資料清洗與爬蟲進度追蹤。  

# 2025/01/02 進度紀錄
[20250102爬蟲程式碼與獲取資料](https://github.com/PeiHsiuLu/Graduation_folio/tree/main/20250102_crawler_record)  
目前已抓取11個網頁資料，每個網頁各抓200筆資料，並將抓取的資料儲存成 json 檔。唯獨 phd_dcard.json 資料僅有63筆，因為 Dcard 博士板資料過少，所以僅能獲取少量資料。  
資料目前抓取的內容分成三種類型：  
1. 升學_海外_留學_考試
2. 閒聊_心情_感情_生活
3. 電影_戲劇綜藝_影音娛樂  
json：  
- title: 文章標題
- link: 文章連結
- content: 文章內容
- comment: 文章留言
- tag: 文章標籤(Dcard的標籤)
- number: 所抓取到的文章編號  
## main.py 程式碼運行所需套件

### 外部 Python 套件
以下套件需要使用 `pip` 安裝：
1. **`undetected-chromedriver`**
   - 用於繞過網站的防自動化檢測，讓 Selenium 更難被檢測到。
   - 安裝指令：
     ```bash
     pip install undetected-chromedriver
     ```

2. **`selenium`**
   - 用於控制瀏覽器進行自動化操作。
   - 安裝指令：
     ```bash
     pip install selenium
     ```

### 標準 Python 套件
以下套件為 Python 標準庫，自帶於 Python 安裝包中，無需額外安裝：
- `threading`：用於多線程操作。
- `logging`：用於記錄程式運行日誌。
- `json`：用於處理 JSON 格式數據。
- `os`：用於處理操作系統功能（如檔案操作）。
- `collections`：用於提供 `OrderedDict` 等集合工具。
- `time`：用於執行延遲操作。
- `random`：用於生成隨機數或隨機延遲。

### 套件安裝總結指令
執行以下指令安裝所有非標準套件：
```bash
pip install undetected-chromedriver selenium
```
## 常見反偵察爬蟲

1. 確認是否為機器人
   目前尚未有好的解決方法，解法就是手動打勾勾：    
   ![image](https://github.com/user-attachments/assets/2eb12049-1c93-49d7-8875-756228441201)   
    
2. Errno 11002  
錯誤指令："urllib.error.URLError: <urlopen error [Errno 11002] getaddrinfo failed>" 代表被 Dcard 偵測到爬蟲，過10-20分鐘後再測試就可以將爬蟲程式碼運行起來，並不代表一定是程式碼有問題。
  
3.爬到文章時出現全白的畫面：
   目前尚未有好的解決方法，所以目前的解決方法是：
- 手動向上滾動，讓頁面文章重新出現
- 重新執行爬蟲程序  
![image](https://github.com/user-attachments/assets/53e6a0ec-a520-458e-bf8b-693bec71636e)

# 2025/01/03 - 2025/01/16 進度紀錄  
主要進行資料清理、模型訓練測試，並持續抓取爬蟲資料。並且根據我們上網抓取的 dcard 爬蟲內容，將聊天機器人進行分類，可參考此資料集：  
[六大聊天機器人分類](https://docs.google.com/spreadsheets/d/1qnFgs3GteaMQ_vWgLvojnvHonovZvJedO9NIpBdtlas/edit?gid=0#gid=0)  
## 模型訓練  
[Llama-3-Taiwan-8B-Instruct模型訓練報告](https://hackmd.io/Ul-Z760DSX2v1Xzb5lSCiA?both)  

## 資料清理
用格式化的方式進行資料處理：先利用 python 將 Dcard 資料處理資料為同一格式，如下：
```json
{
        "instruction": "你是『抱抱熊』，一位 32 歲的心理諮商師，綽號是『溫暖大熊』。你個性溫暖細膩，擅長傾聽，總能在對話中給人安心感。你擅長幫助人們處理情緒問題，並以溫柔而具建設性的方式給予建議。你的興趣包括心理學、MBTI、兩性關係和社交技巧。你熱衷於幫助人們建立更健康的人際關係，提供心理支持與實用建議。請根據以下內容提供溫暖而具啟發性的回應，幫助對方理解自己的情緒與想法。",
        "context": {
            "title": "#發問 紫微斗數問題",
            "tags": [
                "紫微斗數"
            ],
            "content": "我想請問一下 有人知道2025流年 已巳年為什麼我顯示的不是命宮，是兄弟宮？\n跟大家不一樣.."
        },
        "response": [
            "最上面藍色那個就是今年乙巳年的流命\n兄弟宮是你的本命盤的宮位\n中間綠色是大限盤的宮位"
        ]
    }
```
由於模型訓練的關係，必須將資料進行進一步的處裡，"context" 僅保留 "content"(Dcard文章內容)的部分，"response"(Dcard 留言)則是隨機抓取一則留言  
```json
    {
        "instruction": "你是『抱抱熊』，一位 32 歲的心理諮商師，綽號是『溫暖大熊』。你個性溫暖細膩，擅長傾聽，總能在對話中給人安心感。你擅長幫助人們處理情緒問題，並以溫柔而具建設性的方式給予建議。你的興趣包括心理學、MBTI、兩性關係和社交技巧。你熱衷於幫助人們建立更健康的人際關係，提供心理支持與實用建議。請根據以下內容提供溫暖而具啟發性的回應，幫助對方理解自己的情緒與想法。",
        "context": "打1200多箱粉紅\n才5個亮粉\n白癡人生",
        "response": "蛇祭壇抽不到碎片大獎\n3倍券倒是給很多\n但我根本練不完\n超過一半都浪費掉"
    }
```
清理後的 json 檔可以參考：[formatted_data.json](https://github.com/PeiHsiuLu/Graduation_folio/blob/main/0116/formatted_data.json)  
## instruction  
instruction 主要的格式如下：  
你是『聊天機器人角色』，一位 "聊天機器人年齡" 的 "聊天機器人職業"，綽號是『聊天機器人綽號』。"個性以及更進一步地描述"。"興趣以及更進一步地描述"。"請根據：...(對聊天機器人下達符合該角色機器人的指令)  
以聊天機器人"抱抱熊"為範例，範例如下：  
"instruction": "你是『抱抱熊』，一位 32 歲的心理諮商師，綽號是『溫暖大熊』。你個性溫暖細膩，擅長傾聽，總能在對話中給人安心感。你擅長幫助人們處理情緒問題，並以溫柔而具建設性的方式給予建議。你的興趣包括心理學、MBTI、兩性關係和社交技巧。你熱衷於幫助人們建立更健康的人際關係，提供心理支持與實用建議。請根據以下內容提供溫暖而具啟發性的回應，幫助對方理解自己的情緒與想法。"  
# 2025/01/23 進度紀錄   
[Dcard 爬蟲教學]
