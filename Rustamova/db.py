import psycopg2
import json
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

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

def save_certification_to_db(title, obtained, description, image_url, details_dict):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            insert_query = """
                INSERT INTO certifications (title, obtained, description, image_url, details)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (title) DO NOTHING
            """
            cursor.execute(insert_query, (
                title.strip(),
                obtained.strip(),
                description.strip(),
                image_url.strip(),
                json.dumps(details_dict)
            ))
            conn.commit()
            print("Certification data saved to database successfully.")
        except Exception as e:
            print(f"Error saving to database: {e}")
        finally:
            cursor.close()
            conn.close()
