#%%
## paper-organizer 專案初始化碼

# main.py
import argparse
from parser import extract_metadata
from database import PaperDatabase
from exporter import export_bibtex, export_csv
from utils import ensure_directories

DB_PATH = "./data/papers.db"
db = PaperDatabase(DB_PATH)


def main():
    ensure_directories()

    parser = argparse.ArgumentParser(description="📚 論文資料管理工具")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--pdf", required=True)
    add_parser.add_argument("--note", default="")
    add_parser.add_argument("--tags", default="")

    list_parser = subparsers.add_parser("list")
    list_parser.add_argument("--tag", default=None)

    export_parser = subparsers.add_parser("export")
    export_parser.add_argument("--format", choices=["bibtex", "csv"], required=True)

    args = parser.parse_args()

    if args.command == "add":
        metadata = extract_metadata(args.pdf)
        db.add_paper(metadata, args.note, args.tags, args.pdf)
        print("✅ 論文已新增至資料庫")

    elif args.command == "list":
        papers = db.list_papers(tag=args.tag)
        for paper in papers:
            print(f"{paper['id']}: {paper['title']} [{paper['tags']}]")

    elif args.command == "export":
        if args.format == "bibtex":
            export_bibtex(db.fetch_all())
        elif args.format == "csv":
            export_csv(db.fetch_all())


if __name__ == "__main__":
    main()

