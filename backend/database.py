import sqlite3

def init_db():
    conn = sqlite3.connect("backend/data/dictionary.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS words (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT UNIQUE NOT NULL,
            meaning TEXT NOT NULL
        );
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()