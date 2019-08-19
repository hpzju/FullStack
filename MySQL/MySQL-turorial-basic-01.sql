show databases;

create database turorial;

use turorial;

show tables;

create table users1 (user_name varchar(50));

show tables;

show columns from users1;

desc users1;

show create table users1;

insert into users1 (user_name) values ("Bob"), ("Jan"), ("Mary");

select * from users1;

drop table if exists users1;

show tables;

show engines;

show table status;

set default_storage_engine=MyISAM;

show table status;

show engines;

set default_storage_engine=InnoDB;

show engines;