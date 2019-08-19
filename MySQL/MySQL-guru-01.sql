show databases;

drop database turorial;

create database tutorial;

use tutorial;

CREATE TABLE persons (
	first_name VARCHAR(255),
	last_name VARCHAR(255)
);

INSERT INTO persons VALUES ('John', 'Thompson');

SELECT concat(first_name, ' ', last_name) as full_name from persons;

show tables;

select version();

select @@version;

CREATE TABLE IF NOT EXISTS	customer (
	id int auto_increment,
    first_name VARCHAR(100),
	last_name VARCHAR(190),
    address VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(2),
    zip_code varchar(10),    
    primary key (id)
);

INSERT INTO customer VALUES (1, 'John', 'Thompson', 'address', 'NY', 'NY', '1234567890');

SELECT * from customer;

CREATE TABLE IF NOT EXISTS	drink_order (
	id int auto_increment,
    customer_id int,
	drink_description varchar(255),
    primary key (id)
);

INSERT INTO drink_order(customer_id, drink_description) VALUES (1, 'cocktail');

SELECT * from drink_order;

show tables;