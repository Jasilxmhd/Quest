--  Aggregate Functions 

use college;

CREATE TABLE employees (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(100),
    department VARCHAR(50),
    designation VARCHAR(50),
    gender VARCHAR(10),
    salary DECIMAL(10,2),
    city VARCHAR(50),
    joining_date DATE,
    experience INT
);

INSERT INTO employees (emp_name, department, designation, gender, salary, city, joining_date, experience) VALUES
					('Rahul Sharma','IT','Developer','Male',55000,'Delhi','2022-05-10',3),
					('Priya Nair','HR','HR Executive','Female',42000,'Kochi','2021-02-15',5),
					('Amit Kumar','Finance','Accountant','Male',47000,'Mumbai','2020-08-20',6),
					('Sneha Das','IT','Developer','Female',62000,'Bangalore','2019-06-12',7),
					('Arjun Menon','Sales','Sales Executive','Male',39000,'Kochi','2023-01-18',2),
					('Anjali Roy','Marketing','Marketing Executive','Female',48000,'Chennai','2021-09-05',4),
					('Vivek Singh','IT','Tester','Male',51000,'Hyderabad','2022-07-09',3),
					('Meera Joseph','HR','HR Manager','Female',68000,'Kochi','2018-03-21',8),
					('Rohit Verma','Finance','Manager','Male',85000,'Delhi','2017-11-11',10),
					('Neha Kapoor','Sales','Sales Manager','Female',73000,'Mumbai','2019-04-17',7),
					('Kiran Kumar','IT','Developer','Male',59000,'Bangalore','2020-01-30',5),
					('Divya Pillai','Marketing','Designer','Female',46000,'Kochi','2022-10-14',2),
					('Sanjay Rao','IT','Team Lead','Male',92000,'Hyderabad','2016-08-08',11),
					('Asha Thomas','Finance','Accountant','Female',52000,'Chennai','2021-12-25',4),
					('Nikhil Raj','Sales','Sales Executive','Male',41000,'Kochi','2023-03-10',1);


select * from employees;


-- Aggregate Functions
-- avg,count,min,max,sum

select avg(salary) from employees;

select avg(experience) from employees;

select count(emp_id) from employees;

select min(salary) from employees;

select max(salary) from employees;

select * from employees where salary = ( select min(salary) from employees);



-- -------------------------------------------------------------------------


-- Agregate Enhance

select * from employees order by salary;

select * from employees order by salary desc;

select * from employees order by emp_name;

select * from employees where department = "IT" order by experience;

select * from employees order by salary desc limit 5;

select * from  employees order by salary desc,emp_name asc;


-- -----------------------------------------------------------------






	-- GROUP BY
    
select department from employees group by department;

select department from employees group by department order by department;

select department , count(department)as Total_employee from employees group by department;

select department, avg(salary ) as AVG_SALARY from employees group by department;

select city , count(emp_name) from employees group by city;

select department, count(*) from employees where city = 'delhi' and department = 'IT';       -- ----------------

select department, avg(salary ) as AVG_SALARY from employees group by department having avg(salary)>60000;

select avg(experience)as average_experience from employees ;

select emp_name from employees where experience> 5.2000;

select department,count(*) from employees group by department having count(*);



-- Remove Duplicates
select distinct department, city from employees;


select count(distinct department)as uniqe_column from employees;


select avg(salary) from employees as navaneetha;




































































































































































