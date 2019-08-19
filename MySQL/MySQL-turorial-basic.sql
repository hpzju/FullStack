show databases;

create database turorial;

use turorial;

show tables;

create table users (user_name varchar(50));

show tables;

show columns from users;

desc users;

show create table users;

insert into users (user_name) values ("Bob"), ("Jan"), ("Mary");

select * from users;

drop table if exists users;

show tables;
