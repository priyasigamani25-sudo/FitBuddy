from pathlib import Path
import sqlite3


DB_PATH = Path("data/fitbuddy.db")


def init_db():
    DB_PATH.parent.mkdir(exist_ok=True)

    conn = sqlite3.connect(DB_PATH)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            height REAL,
            weight REAL
        )
    """)

    conn.commit()
    conn.close()