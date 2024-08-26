Simple python server + postgreSQL + haproxy  

запуск приложения - **docker compose up**  

+ **simple_server** - сервер, который ожидает входящее соединение и создает базу
+ **db** - база данных
+ **haproxy** - проксирует запросы к simple_server и db
+ **client_cheker** - клиент, который обращается к серверу для создания базы и выполняет несколько запросов в БД
 
