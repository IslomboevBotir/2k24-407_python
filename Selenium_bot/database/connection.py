import psycopg2

def get_connection():
    try:
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="1234",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"PostgreSQL ulanishida xato: {e}")
        raise