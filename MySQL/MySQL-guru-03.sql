use employees;

select * from employees 
inner join dept_manager
on employees.emp_no = dept_manager.emp_no;
 
SELECT dept_name, emp.emp_no, first_name, last_name FROM
employees AS emp
 JOIN 
 dept_manager AS dm
 ON emp.emp_no = dm.emp_no
 JOIN 
 departments AS dept
 ON dm.dept_no = dept.dept_no
WHERE
 dm.to_date = '9999-01-01' 
order by dept_name; 
 
SELECT dept_name, emp.emp_no, first_name, last_name FROM
employees AS emp
 JOIN 
 dept_manager AS dm
 ON emp.emp_no = dm.emp_no
 JOIN 
 departments AS dept
 ON dm.dept_no = dept.dept_no
WHERE
 dm.to_date = '9999-01-01' 
 AND emp.gender = 'F'
order by dept_name;  
 
SELECT dept_name, emp.emp_no, first_name, last_name FROM
employees AS emp
 JOIN 
 dept_manager AS dm
 ON emp.emp_no = dm.emp_no
 JOIN 
 departments AS dept
 ON dm.dept_no = dept.dept_no
WHERE
 dm.to_date = '9999-01-01' 
 AND emp.gender = 'M'
order by dept_name;  

use northwind;
  
SELECT 
    cust.first_name AS 'First Name',
    cust.last_name AS 'Last Name',
    ord.ship_address AS 'Street',
    ord.ship_city AS 'City',
    ord.ship_state_province AS 'State',
    ord.ship_zip_postal_code AS 'Zip',
    ord.ship_country_region AS 'Country',
    shippers.company AS 'Shipper',
    DATE_FORMAT(ord.order_date, '%M %D %Y') AS 'Order Date',
    products.product_code AS 'Product Code',
    products.product_name AS 'Product Name',
    FORMAT(ord_det.quantity, 0) AS 'Qty Ordered',
    FORMAT(products.standard_cost, 2) AS 'Cost',
    FORMAT(ord_det.quantity * products.standard_cost,
        2) AS 'Total Cost'
FROM
    orders AS ord
        JOIN
    order_details AS ord_det ON ord.id = ord_det.order_id
        JOIN
    customers AS cust ON ord.customer_id = cust.id
        JOIN
    shippers ON shippers.id = ord.shipper_id
        JOIN
    products ON ord_det.product_id = products.id;