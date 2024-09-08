Simple python server FastAPI + PostgreSQL + HAProxy  

запуск приложения - **docker compose up**  

+ **simple_server** - сервер, который ожидает входящее соединение и создает базу
+ **db** - база данных
+ **haproxy** - проксирует запросы к simple_server и db
 
