from database.connection import get_connection

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id SERIAL PRIMARY KEY,
            title TEXT,
            image TEXT,
            text TEXT,
            publish_date TEXT,
            link TEXT,
            tools_type TEXT
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()

def insert_post(title, image, text, publish_date, link, tools_type):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO posts (title, image, text, publish_date, link, tools_type)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (title, image, text, publish_date, link, tools_type))
    conn.commit()
    cursor.close()
    conn.close()