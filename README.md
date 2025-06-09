<<<<<<< HEAD
# paper-organizer
=======
>>>>>>> b36b5a4 (Initial commit)
# README.md
# 📚 Paper Organizer

管理你的論文 PDF 檔案，匯出 BibTeX、CSV 格式。
## 🛠 安裝
```bash
pip install -r requirements.txt
```

## 📂 專案結構
```
paper-organizer/
├── main.py              # 程式進入點：CLI 啟動
├── parser.py            # 解析 PDF metadata
├── database.py          # SQLite 操作
├── exporter.py          # BibTeX / CSV 匯出
├── utils.py             # 建立資料夾等工具
├── papers/              # 儲存原始 PDF
├── data/                # SQLite 資料庫與匯出檔案
├── requirements.txt     # 套件需求
└── README.md            # 說明文件
```
<<<<<<< HEAD
=======

## 🚀 使用方式
```bash
# 加入 PDF 論文檔案
python main.py add --pdf papers/example.pdf --note "Janus TMD" --tags "2D,MoSSe"

# 列出所有論文
python main.py list

# 匯出 BibTeX
python main.py export --format bibtex

# 匯出 CSV
python main.py export --format csv
```
>>>>>>> b36b5a4 (Initial commit)
