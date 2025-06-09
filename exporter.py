#%%
# exporter.py
import csv
from jinja2 import Template
import os

BIBTEX_TEMPLATE = Template("""
@article{{{{ bibkey }}}},
  title={{"{{ title }}"}},
  author={{"{{ authors }}"}},
  journal={{"{{ journal }}"}},
  year={{ {{ year }} }},
  note={{"{{ note }}"}}
}}
""")

def export_bibtex(papers, output="./data/export.bib"):
    with open(output, "w", encoding="utf-8") as f:
        for i, p in enumerate(papers):
            entry = BIBTEX_TEMPLATE.render(
                bibkey=f"paper{i+1}",
                title=p['title'],
                authors=p['authors'],
                journal=p['journal'],
                year=p['year'],
                note=p['note']
            )
            f.write(entry + "\n")
    print(f"✅ BibTeX 匯出成功：{output}")

def export_csv(papers, output="./data/export.csv"):
    with open(output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=papers[0].keys())
        writer.writeheader()
        writer.writerows(papers)
    print(f"✅ CSV 匯出成功：{output}")