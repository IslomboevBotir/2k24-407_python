import json
from .connection import connect_to_db

def save_project_to_db(title, date, description, image_url, type_badges, technologies, project_links):
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            query = """
                INSERT INTO projects (title, date_range, description, image_url, type_badges, technologies, project_links)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                title, date, description, image_url,
                json.dumps(type_badges),
                json.dumps(technologies),
                json.dumps(project_links)
            ))
            conn.commit()
            print("✅ Saved to DB.")
        except Exception as e:
            print(f"❌ Insert error: {e}")
        finally:
            cursor.close()
            conn.close()
