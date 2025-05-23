import sqlite3
import os


def init_database():
    try:
        if os.path.exists("posts.db"):
            os.remove("posts.db")

        conn = sqlite3.connect("posts.db")
        cursor = conn.cursor()

        cursor.execute("""
                       CREATE TABLE posts
                       (
                           id           INTEGER PRIMARY KEY AUTOINCREMENT,
                           title        TEXT,
                           subtitle     TEXT,
                           image_url    TEXT,
                           publish_date DATE,
                           link         TEXT,
                           full_content TEXT
                       )
                       """)

        conn.commit()
        conn.close()

    except Exception as e:
        pass


def save_post(title, subtitle, image_url, publish_date, link, full_content):
    try:
        conn = sqlite3.connect("posts.db")
        cursor = conn.cursor()

        cursor.execute("""
                       INSERT INTO posts (title, subtitle, image_url, publish_date, link, full_content)
                       VALUES (?, ?, ?, ?, ?, ?)
                       """, (title, subtitle, image_url, publish_date, link, full_content))

        conn.commit()
        conn.close()

    except Exception as e:
        pass


def get_all_posts():
    try:
        conn = sqlite3.connect("posts.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM posts")
        posts = cursor.fetchall()

        conn.close()
        return posts

    except Exception as e:
        return []

