import sqlite3
from typing import Tuple

class Database:

    def __init__(self, db_name: str = "lab.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS data_lab
            (
                title
                VARCHAR,
                created_at
                VARCHAR,
                image_url
                TEXT,
                image_description
                VARCHAR,
                all_description
                VARCHAR
            )
            """
        )
        self.connection.commit()

    def insert_data(self, title: str, created_at: str, image_url: str,
                    image_description: str, all_description: str):
        try:
            self.cursor.execute(
                """
                INSERT INTO data_lab (title, created_at, image_url, image_description, all_description)
                VALUES (?, ?, ?, ?, ?)
                """,
                (title, created_at, image_url, image_description, all_description)
            )
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            self.connection.rollback()

    def close(self):
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()