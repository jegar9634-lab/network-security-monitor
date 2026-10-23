import sqlite3
from pathlib import Path
from datetime import datetime

DB_PATH = Path(__file__).parent / "network_monitor.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL,
                severity TEXT NOT NULL,
                title TEXT NOT NULL,
                details TEXT NOT NULL,
                local_address TEXT NOT NULL
            )
        """)

def save_events(events):
    if not events:
        return
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rows = [
        (now, e["severity"], e["title"], e["details"], e["local_address"])
        for e in events
    ]
    with sqlite3.connect(DB_PATH) as conn:
        conn.executemany("""
            INSERT INTO events
            (created_at, severity, title, details, local_address)
            VALUES (?, ?, ?, ?, ?)
        """, rows)

def get_recent_events(limit=100):
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute("""
            SELECT created_at, severity, title, details, local_address
            FROM events ORDER BY id DESC LIMIT ?
        """, (limit,)).fetchall()
        return [dict(row) for row in rows]
