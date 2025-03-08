# PDF 內容提取與 AI 問答系統

這是一個使用 Flask 框架和 OpenAI API 的專案，旨在從 PDF 文件中提取文本並根據用戶的問題提供相關的回答。

## 目錄

- [功能](#功能)
- [安裝](#安裝)
- [使用方法](#使用方法)
- [貢獻](#貢獻)
- [許可證](#許可證)

## 功能

- 從指定資料夾中的 PDF 文件提取文本。
- 根據用戶的問題檢索相關內容。
- 使用 OpenAI 的 GPT 模型生成回答。

## 安裝

1. 確保您已安裝 Python 3.x。
2. 克隆此倉庫：
   ```bash
   git clone YOUR_GITHUB_URL
   ```
3. 進入專案目錄：
   ```bash
   cd YOUR_PROJECT_DIRECTORY
   ```
4. 安裝所需的依賴：
   ```bash
   pip install -r requirements.txt
   ```
5. 創建一個 `.env` 文件，並添加您的 OpenAI API 金鑰：
   ```plaintext
   OPENAI_API_KEY=your_api_key_here
   ```

## 使用方法

1. 啟動 Flask 應用：
   ```bash
   python app.py
   ```
2. 在瀏覽器中訪問 `http://127.0.0.1:5000/`。
3. 在頁面上輸入您的問題，系統將根據 PDF 文件中的內容提供回答。

## 貢獻

歡迎任何形式的貢獻！請提交問題或拉取請求。

## 許可證

此專案使用 MIT 許可證。詳情請參見 [LICENSE](LICENSE) 文件。"# PDF-AI" 
"# PDF-AI" 
