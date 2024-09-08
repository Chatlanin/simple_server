import psycopg2
import database as db


def db_connect(db_name="postgres"):
    try:
        conn = psycopg2.connect(
            user="postgres",
            database=db_name,
            password="secret_pass",
            host="db",
            port=5432,
        )
    except psycopg2.OperationalError:
        print(f"Database {db_name} does not exist")
        return
    return conn


conn = db_connect(db_name="pbx_refactor")
if not conn:
    conn = db_connect()
    conn.autocommit = True
    db.create_db(conn, "pbx_refactor")
    conn.close()

conn = db_connect(db_name="pbx_refactor")
conn.autocommit = True
db.create_table(conn, "some_table")
conn.close()
