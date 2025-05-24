import psycopg2
from psycopg2 import Error


class DatabaseManager:
    def __init__(self, db_config):
        self.db_config = db_config
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host=self.db_config["host"],
                port=self.db_config["port"],
                database=self.db_config["database"],
                user=self.db_config["user"],
                password=self.db_config["password"],
            )
            self.cursor = self.conn.cursor()

            create_table_query = """
            CREATE TABLE IF NOT EXISTS certifications (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                date VARCHAR(100),
                image_url TEXT,
                description TEXT,
                extra_description JSON
            );
            """
            self.cursor.execute(create_table_query)
            self.conn.commit()
            print("Table 'certifications' is ready.")
        except Error as e:
            print(f"Error connecting to database: {e}")
            self.conn = None
            self.cursor = None

    def save_certification(self, data):
        if not data:
            print("No data to save.")
            return

        if not self.conn or not self.cursor:
            print("No database connection.")
            return

        try:
            insert_query = """
            INSERT INTO certifications (title, date, image_url, description, extra_description)
            VALUES (%s, %s, %s, %s, %s);
            """
            self.cursor.execute(
                insert_query,
                (
                    data.get("title", ""),
                    data.get("date", ""),
                    data.get("image_url", ""),
                    data.get("description", ""),
                    data.get("extra_description", ""),
                ),
            )
            self.conn.commit()
            print("Data saved to PostgreSQL successfully.")
        except Error as e:
            print(f"Error saving to PostgreSQL: {e}")
            self.conn.rollback()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            print("Database connection closed.")
