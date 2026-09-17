"""Persistent text memory backed by the Python standard library."""

import sqlite3
from pathlib import Path


class SQLiteMemory:
    def __init__(self, path: str | Path = "memory.db"):
        self.connection = sqlite3.connect(str(path))
        self.connection.execute("CREATE TABLE IF NOT EXISTS memories (id INTEGER PRIMARY KEY, text TEXT NOT NULL, created_at TEXT DEFAULT CURRENT_TIMESTAMP)")
        self.connection.commit()

    def add(self, text: str) -> int:
        cursor = self.connection.execute("INSERT INTO memories(text) VALUES (?)", (text,))
        self.connection.commit()
        return int(cursor.lastrowid)

    def recent(self, limit: int = 10) -> list[str]:
        rows = self.connection.execute("SELECT text FROM memories ORDER BY id DESC LIMIT ?", (max(limit, 0),)).fetchall()
        return [row[0] for row in rows]

    def close(self) -> None:
        self.connection.close()
