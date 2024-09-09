Simple python server FastAPI + PostgreSQL + HAProxy  

запуск приложения - **docker compose up**  

+ **simple_server** - сервер, который ожидает входящее соединение и создает базу
+ **db** - база данных
+ **haproxy** - проксирует запросы к simple_server и db

Сервер доступен на порту 1111, для сервера доступно два эндпонита:
+ /get_data - получить данные из БД
+ /put_data - записать рандомные данные в БД
 
