#%%
# parser.py
import fitz  # PyMuPDF
import os

def extract_metadata(pdf_path):
    doc = fitz.open(pdf_path)
    meta = doc.metadata

    # 嘗試從內容取得標題與作者
    text = doc[0].get_text()
    title = meta.get("title") or text.split("\n")[0][:100]
    author = meta.get("author") or "Unknown"

    return {
        "title": title.strip(),
        "authors": author.strip(),
        "journal": meta.get("subject") or "",
        "year": meta.get("creationDate", "0000")[:4],
        "doi": meta.get("doi", "")
    }
