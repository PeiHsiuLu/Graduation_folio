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

錯誤指令："urllib.error.URLError: <urlopen error [Errno 11002] getaddrinfo failed>" 代表被 Dcard 偵測到爬蟲，過幾分鐘再測試就可以將爬蟲程式碼運行起來  
