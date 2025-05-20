import sqlite3
import logging

# Logging sozlash
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def get_connection():
    """Bazaga ulanish hosil qiladi."""
    return sqlite3.connect("certifications.db")


def create_certification_table():
    """Agar mavjud bo'lmasa jadvalni yaratadi."""
    try:
        with get_connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS certifications (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    header TEXT NOT NULL,
                    date TEXT,
                    image TEXT,
                    description TEXT
                )
            """)
            logging.info("✅ Jadval yaratildi yoki allaqachon mavjud.")
    except sqlite3.Error as e:
        logging.error(f"❌ Jadval yaratishda xatolik: {e}")
