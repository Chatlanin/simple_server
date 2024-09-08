from psycopg2.errors import DuplicateDatabase
import random


def create_db(conn, name):
    with conn.cursor() as cursor:
        try:
            cursor.execute(f"create database {name}")
            print(f"Database {name} create successfully")
            return True
        except DuplicateDatabase:
            print(f"Database {name} already exists")


def create_table(conn, name):
    with conn.cursor() as cursor:
        cursor.execute(
            f"create table if not exists {name} (id serial primary key, value character varying(30))"
        )


def get_data(conn, db_name="some_table", limit=3):
    with conn.cursor() as cursor:
        cursor.execute(f"select * from {db_name} order by id desc limit {limit}")
        return cursor.fetchall()


def put_data(conn, db_name="some_table"):
    data = random.randrange(0, 10000000)
    with conn.cursor() as cursor:
        cursor.execute(f"insert into {db_name} values (default, {data})")
    return data
