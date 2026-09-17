from pathlib import Path
from tempfile import TemporaryDirectory

from neural_lab.sqlite_memory import SQLiteMemory


with TemporaryDirectory() as directory:
    store = SQLiteMemory(Path(directory) / "demo.db")
    store.add("Persistent memory survives beyond an in-memory agent step.")
    store.add("SQLite is useful for small local AI experiments.")
    for item in store.recent():
        print(item)
    store.close()
