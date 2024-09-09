from fastapi import FastAPI
import psycopg2
import database as db
import uvicorn


app = FastAPI()


def get_connect():
    conn = psycopg2.connect(
        user="postgres",
        database="pbx_refactor",
        password="secret_pass",
        host="haproxy",
        port=5432,
    )
    conn.autocommit = True
    return conn


@app.get("/get_data")
def get_data():
    conn = get_connect()
    response = db.get_data(conn)
    conn.close()
    return response


@app.get("/put_data")
def put_data():
    conn = get_connect()
    response = db.put_data(conn)
    conn.close()
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1234)
