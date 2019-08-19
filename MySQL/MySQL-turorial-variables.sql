select @@global.sql_mode;
set sql_mode = 'STRICT_ALL_TABLES';
select @@global.sql_mode;

select @@session.sql_safe_updates;
set sql_safe_updates = 0;
select @@session.sql_safe_updates;

set autocommit = 1;
select @@autocommit;