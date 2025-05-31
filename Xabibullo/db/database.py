import json
import psycopg2

DB_HOST = "localhost"
DB_NAME = "selenium"
DB_USER = "postgres"
DB_PASSWORD = "postgres"

def connect_to_db():
    try:
        return psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
    except Exception as e:
        print(f"Database connection error: {e}")
        return None

def create_table_if_not_exists():
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            create_query = """
                CREATE TABLE IF NOT EXISTS certifications (
                    id SERIAL PRIMARY KEY,
                    title TEXT NOT NULL,
                    obtained TEXT,
                    description TEXT,
                    image_url TEXT,
                    details JSONB,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """
            cursor.execute(create_query)
            conn.commit()
            print("✅ Jadval tayyor yoki mavjud.")
        except Exception as e:
            print(f"❌ Jadval yaratishda xatolik: {e}")
        finally:
            cursor.close()
            conn.close()

def save_certification_to_db(title, obtained, description, image_url, details_dict):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            insert_query = """
                INSERT INTO certifications (title, obtained, description, image_url, details)
                VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (
                title.strip(),
                obtained.strip(),
                description.strip(),
                image_url.strip(),
                json.dumps(details_dict)
            ))
            conn.commit()
            print("✅ Ma’lumotlar bazaga saqlandi.")
        except Exception as e:
            print(f"❌ Saqlashda xatolik: {e}")
        finally:
            cursor.close()
            conn.close()
    else:
        print("❌ Bazaga ulanishda muammo bor.")
