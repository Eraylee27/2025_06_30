# Copilot 指令（針對 lesson21）

## 專案概述
這是一個基於 Flask 的網站專案，使用 Bootstrap 5 前端框架，採用標準的 MVC 架構設計。

## 核心組件
1. **後端 (`app.py`)**
   - Flask 路由和視圖邏輯
   - 環境變數配置（使用 python-dotenv）
   - 開發模式啟用（自動重載）

2. **前端模板 (`templates/`)**
   - 使用 Jinja2 模板引擎
   - Bootstrap 5 為主要 UI 框架
   - 響應式設計支援

3. **靜態資源 (`static/`)**
   - CSS：`static/css/style.css`（自定義樣式）
   - 圖片：`static/images/`（如有需要）

## 開發環境
### 必要條件
- conda 環境：`data`
- Python：3.12.11
- 套件需求：見 `requirements.txt`

### 快速開始
```bash
# 1. 啟動環境
conda activate data

# 2. 安裝依賴
pip install -r requirements.txt

# 3. 執行應用
python app.py
```

## 專案慣例
1. **模板結構**
   - 基礎模板：`templates/index.html`
   - 導覽列使用 Bootstrap navbar
   - 頁面主體使用 container 類別

2. **樣式規範**
   - 使用 Bootstrap 類別優先
   - 自定義樣式位於 `static/css/style.css`
   - RWD 斷點遵循 Bootstrap 標準

3. **路由命名**
   - 主頁：`@app.route('/')`
   - 視圖函數使用語意化命名（如：`home`）

## 開發工作流程
1. 修改模板：編輯 `templates/` 下的 HTML 檔案
2. 更新樣式：編輯 `static/css/style.css`
3. 添加路由：在 `app.py` 中定義新路由
4. 測試：訪問 http://localhost:5000

