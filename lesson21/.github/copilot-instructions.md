## Repo 簡介 (big picture)

這個 repository 是一個小型練習/教學專案，包含數個簡單的 Python 檔案與筆記本：

- `lesson21_2.py`：單行示範腳本（會印出 `Hello, World!`），適合作為快速執行測試。
- `lesson21_1.ipynb`：Jupyter 筆記本，可能含有互動示例。
- `AGENTS.md`：專案為執行腳本/筆記本提供的運行前說明（例如啟用 conda 環境）。

結構很扁平，主要工作流為啟動 conda 環境後直接執行 Python 檔或打開 notebook。

## 主要工作流程（必須知道的命令）

- 啟動 conda env（強制）：

  ```cmd
  conda activate data
  ```

- 執行練習腳本（範例）：

  ```cmd
  python lesson21_2.py
  ```

- 打開筆記本：使用 VS Code 或 Jupyter 開啟 `lesson21_1.ipynb`。

註：`AGENTS.md` 明確要求在執行前啟用 `data` 環境；AI agent 在自動執行前應先確認並遵守此步驟。

## 對 AI agent 的具體指令（短而可執行）

1. 進入 repo 根目錄（本專案底下的 `lesson21`）再執行任何程式。
2. 在執行腳本或 notebook 前，確認使用者或環境已執行 `conda activate data`。若 agent 無法切換環境，應直接回報並請求授權或由使用者在 terminal 執行。
3. 先讀取並解析 `AGENTS.md`，找到任何運行前的要求並遵守（例如環境名稱）。
4. 小變更或修正應先在本地運行（或在 sandbox）並把 stdout/stderr 重導到檔案以便回傳結果，例如：

  ```cmd
  python lesson21_2.py > out.txt 2>&1
  type out.txt
  ```

5. 若要修改程式碼，請用小步驟：修改 -> 執行 -> 回傳變更摘要與測試輸出。

## 專案約定與可觀察模式（從檔案可推斷）

- 這個專案沒有複雜的模組化或封裝；程式多為單檔腳本或 notebook。AI agent 不應嘗試大幅重構，除非使用者明確要求。
- 無測試框架（`pytest` 或類似）在 repo 中可見；新增測試屬於可選的價值加成，但不是先決要求。
- 專案使用 conda 管理環境（見 `AGENTS.md`），因此任何自動執行步驟都應尊重 conda 環境切換。

## 常見任務示例（具體到本 repo）

- 要驗證程式能執行並返回預期輸出：先 `conda activate data`，再 `python lesson21_2.py`，預期 stdout 為 `Hello, World!`。
- 若使用者請求我幫忙執行並回傳輸出，請在執行後把 stdout/stderr 寫入 `out.txt` 並讀取該檔案內容回報給使用者。

## 何時要求使用者介入（失敗或限制時）

- 若 agent 無法切換或啟用 conda 環境，應立即回報並請使用者在 terminal 執行 `conda activate data`。
- 若執行需要外部秘密或網路存取（此 repo 目前無此類需求），不要自行嘗試存取，先詢問使用者。

## 參考檔案

- `AGENTS.md`：必讀，列出「執行前請先啟用 conda 環境」的要求。
- `lesson21_2.py`：最小可執行示例，AI agent 可用來驗證基本執行鏈。
- `lesson21_1.ipynb`：如需深入互動示例，優先以 notebook 檢視內容。

---

如果這份指引有需要補充的地方（例如你想讓 agent 自動建立 `out.txt` 的命名規則或要我把筆記本輸出自動轉成 HTML），請告訴我想要的細節，我會立刻更新。 
