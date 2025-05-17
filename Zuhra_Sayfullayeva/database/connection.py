import psycopg2
from config.settings import DB_CONFIG

def connect_to_db():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"❌ DB Connection Error: {e}")
        return None
