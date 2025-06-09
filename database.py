#%%
# database.py
import sqlite3

class PaperDatabase:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        self.conn.execute('''CREATE TABLE IF NOT EXISTS papers (
            id INTEGER PRIMARY KEY,
            title TEXT,
            authors TEXT,
            journal TEXT,
            year TEXT,
            doi TEXT,
            note TEXT,
            tags TEXT,
            path TEXT
        )''')
        self.conn.commit()

    def add_paper(self, metadata, note, tags, path):
        self.conn.execute('''INSERT INTO papers 
            (title, authors, journal, year, doi, note, tags, path)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
            (metadata['title'], metadata['authors'], metadata['journal'], metadata['year'],
             metadata['doi'], note, tags, path))
        self.conn.commit()

    def list_papers(self, tag=None):
        cursor = self.conn.cursor()
        if tag:
            cursor.execute("SELECT * FROM papers WHERE tags LIKE ?", (f"%{tag}%",))
        else:
            cursor.execute("SELECT * FROM papers")
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def fetch_all(self):
        return self.list_papers()