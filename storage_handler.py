# SQLite3 based storage handling user session progress

import sqlite3

class StorageHandler:
    def __init__(self, db_path="gleam.db"):
        self.conn = sqlite3.connect(db_path)
        self.init_tables()

    def init_tables(self):
        c = self.conn.cursor()
        c.execute(
            """
            CREATE TABLE IF NOT EXISTS sessions (
                user_id TEXT PRIMARY KEY,
                score INTEGER,
                streak INTEGER
            )
            """
        )
        self.conn.commit()

    def save_score(self, user_id, score, streak=0):
        c = self.conn.cursor()
        c.execute(
            """
            INSERT INTO sessions (user_id, score, streak)
            VALUES (?, ?, ?)
            ON CONFLICT(user_id) DO UPDATE SET
            score=excluded.score,
            streak=excluded.streak
            """,
            (user_id, score, streak),
        )
        self.conn.commit()

    def get_score(self, user_id):
        c = self.conn.cursor()
        c.execute("SELECT score, streak FROM sessions WHERE user_id=?", (user_id,))
        row = c.fetchone()
        if row:
            return {'score': row[0], 'streak': row[1]}
        return None