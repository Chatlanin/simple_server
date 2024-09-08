from fastapi import FastAPI
import psycopg2
import database as db
import uvicorn


app = FastAPI()
conn = psycopg2.connect(
    user="postgres",
    database="pbx_refactor",
    password="secret_pass",
    host="db",
    port=5432,
)
conn.autocommit = True


@app.get("/get_data")
def get_data():
    return db.get_data(conn)


@app.get("/put_data")
def put_data():
    response = db.put_data(conn)
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1234)
