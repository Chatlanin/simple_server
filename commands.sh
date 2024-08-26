#!/bin/bash
curl haproxy:80
psql -h haproxy -U postgres -p 5000 -d pbx_refactor -c 'create table some_table (id serial primary key, value character varying(30))'
psql -h haproxy -U postgres -p 5000 -d pbx_refactor -c "insert into some_table values (default, '$(hostname)')"
psql -h haproxy -U postgres -p 5000 -d pbx_refactor -c "select * from some_table"
