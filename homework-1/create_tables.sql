-- SQL-команды для создания таблиц

CREATE TABLE employees
(
	employee_id varchar(100) PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(150),
	birth_date varchar(150),
	notes text
);

CREATE TABLE customers
(
	customer_id varchar(100) PRIMARY KEY,
	company_name varchar(200) NOT NULL,
	contact_name text
);

CREATE TABLE orders
(
	order_id varchar(100) PRIMARY KEY,
	customer_id varchar(100) REFERENCES customers(customer_id) NOT NULL,
	employee_id varchar(100) REFERENCES employees(employee_id) NOT NULL,
	order_date varchar(150),
	ship_city varchar(100)
);

