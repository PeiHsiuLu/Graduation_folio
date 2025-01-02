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

