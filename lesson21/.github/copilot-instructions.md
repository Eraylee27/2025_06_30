# Copilot 指令（針對 lesson21）

## 專案概述
這是一個基本的 Flask Web 應用專案，提供簡單的網頁服務功能。

## 環境設置
### Python 環境
- 使用 conda 環境：`data`
- Python 版本：3.12.11
- 執行前必須啟動環境：`conda activate data`

### 依賴套件
主要套件（詳見 `requirements.txt`）：
- Flask 3.1.2
- python-dotenv 1.1.1

## 專案架構
```
lesson21/
├── app.py              # Flask 應用主程式
├── requirements.txt    # 相依套件列表
├── static/            # 靜態檔案目錄
└── templates/         # HTML 模板目錄
```

## 開發工作流程
1. **環境準備**：
   ```bash
   conda activate data
   ```

2. **安裝依賴**：
   ```bash
   pip install -r requirements.txt
   ```

3. **執行應用**：
   ```bash
   python app.py
   ```

## 注意事項
- 開發模式已啟用（debug=True）
- 應用程式預設運行在 http://localhost:5000
- 靜態檔案應放在 `static/` 目錄
- HTML 模板應放在 `templates/` 目錄

