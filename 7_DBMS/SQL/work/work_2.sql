
USE work;

CREATE TABLE employees ( 
						emp_id INT PRIMARY KEY, 
						emp_name VARCHAR(100), 
						department VARCHAR(50), 
						designation VARCHAR(50), 
						gender VARCHAR(10), 
						salary DECIMAL(10,2), 
						city VARCHAR(50), 
						joining_date DATE, 
						experience INT 
);


INSERT INTO employees VALUES 
								(101,'Rahul Sharma','IT','Developer','Male',55000,'Kochi','2021-01-15',4), 
								(102,'Anjali Nair','HR','HR Executive','Female',42000,'Kozhikode','2020-06-10',6), 
								(103,'Akhil Das','Finance','Accountant','Male',48000,'Thrissur','2019-09-22',7), 
								(104,'Meera Pillai','IT','Developer','Female',61000,'Kochi','2022-03-18',3), 
								(105,'John Mathew','Sales','Sales Executive','Male',45000,'Kottayam','2021-11-02',4), 
								(106,'Sneha R','Marketing','Marketing Executive','Female',47000,'Kannur','2023-01-09',2), 
								(107,'Arun Kumar','IT','Tester','Male',39000,'Palakkad','2022-07-14',3), 
								(108,'Diya Joseph','Finance','Analyst','Female',65000,'Ernakulam','2018-12-01',8), 
								(109,'Nithin Raj','Sales','Manager','Male',78000,'Kochi','2017-08-20',9), 
								(110,'Fathima K','HR','Manager','Female',70000,'Malappuram','2016-04-12',10); 
                                
                                
                                
-- 1. Display all employee names in uppercase.
select upper(emp_name) as Employees_Name from employees;



-- 2. Display all employee names in lowercase.
select lower(emp_name) as Employees_Name from employees;




-- 3. Find the length of each employee name.
select emp_name,length(emp_name) as Length from employees;



-- 4. Display the first 3 characters of each employee name.
select emp_name, left(emp_name,3)as First_3_characters from employees;



--  5. Display the last 4 characters of each employee name.
select emp_name, right(emp_name,4)as Last_4_characters from employees;



-- 6. Concatenate employee name and city.
select concat(emp_name, ' - ' , city)as emp_city from employees;




-- 7. Replace 'Developer' with 'Software Engineer' in designation.

                                
select * from employees;
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                