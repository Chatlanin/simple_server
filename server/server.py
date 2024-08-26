import socketserver
import psycopg2

HOST, PORT = "0.0.0.0", 1234

conn = psycopg2.connect(
    user="postgres", password="secret_pass", host="haproxy", port=5000
)
conn.autocommit = True


class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        with conn.cursor() as cursor:
            cursor.execute("create database pbx_refactor")
        conn.close()
        print("Создали базу")


with socketserver.TCPServer((HOST, PORT), TCPHandler) as socket:
    socket.handle_request()
