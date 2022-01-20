import sqlite3

class KomikkuParser:
    """
    TODO
    """
    db: sqlite3.Connection
    def __init__(self, path: str):
        self.db = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
