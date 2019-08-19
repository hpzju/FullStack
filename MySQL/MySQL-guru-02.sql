use employees;
select count(*) as num_employees from employees;
select count(*) num_salaries from salaries;
select count(*) num_titles from titles;
select count(*) num_departments from departments;
select count(*) num_dept_emp from dept_emp;
select count(*) num_dept_manager from dept_manager;

SELECT * FROM employees;

SELECT 
    first_name, last_name
FROM
    employees;

SELECT 
    emp_no, salary
FROM
    salaries;
    
select curdate();

select * from employees where first_name = 'Elvis';

select count(*) as Num_female from employees where gender = 'F';

SELECT first_name, last_name FROM employees;

SELECT emp_no, salary FROM salaries;

SELECT first_name as 'First Name', last_name as 'Last Name' FROM employees;

SELECT first_name, last_name, concat(first_name, ' ', last_name) as 'Name' FROM employees;

SELECT salary, 
salary * .01 as weekly,
salary * .01 * 4 as monthly,
salary * .01 * 52 as yearly  FROM salaries;

SELECT from_date as original, DATE_FORMAT(from_date, "%M %d %Y") FROM salaries; 

SELECT first_name, last_name, 
concat(LEFT(first_name, 1), LEFT(last_name, 1)) as Initials from employees;

SELECT * FROM employees WHERE first_name = 'Elvis' and last_name = 'Velasco'
or first_name = 'Chenye' and last_name = 'Velasco';

SELECT * FROM employees WHERE first_name IN ('Elvis', 'Sumant','Berni', 'Lillian' );

select * from employees where first_name LIKE 'Elv%' and last_name LIKE '_e%';

select * from employees where birth_date between  '1954-05-01' and '1956-04-20';

select * from employees order by first_name DESC;

select * from employees order by emp_no LIMIT  20, 88;

select * from salaries;

select first_name, count(*) as emp_count from employees group by first_name;

select first_name, count(*) as emp_count from employees group by first_name having emp_count > 250;

select salary, count(*) as sal_count from salaries group by salary having sal_count > 100 order by sal_count asc;

select salary, count(*) as sal_count 
from salaries 
where from_date > '1994-06-24'
group by salary 
having sal_count > 50 
order by sal_count asc;