CREATE DATABASE IF NOT EXISTS company_db;
USE company_db;

CREATE TABLE IF NOT EXISTS employees(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    hire_date DATE NOT NULL,
    city VARCHAR(50) NOT NULL
);

INSERT INTO employees (name, department, salary, hire_date, city) VALUES
                                                                      ('Aarav	Sharma', 'Engineering',	85000.00, '2022-03-15',	'Bangalore'),
('Priya Nair', 'Engineering', 92000.00, '2021-07-01', 'Bangalore'),
('Rohan Mehta','Sales', 60000.00, '2023-01-10', 'Mumbai'),
('Sneha Iyer', 'Sales', 65000.00, '2020-11-20', 'Mumbai'),
('Vikram Singh', 'Marketing', 55000.00, '2022-06-05', 'Delhi'),
('Ananya Rao', 'Marketing', 58000.00, '2023-09-12', 'Delhi'),
('Karan Malhotra', 'Engineering', 98000.00, '2019-04-22', 'Bangalore'),
('Divya Menon', 'HR', 50000.00, '221-02-18', 'Chennai'),
('Arjun Reddy', 'HR', 52000.00, '2022-12-01', 'Chennai'),
('Neha Gupta', 'Sales', 70000.00, '2020-08-30', 'Mumbai'),
('Sameer Khan', 'Engineering', 88000.00, '2023-05-14', 'Bangalore'),
('Ritu Kapoor', 'Marketing', 61000.00, '2021-10-09', 'Delhi');
