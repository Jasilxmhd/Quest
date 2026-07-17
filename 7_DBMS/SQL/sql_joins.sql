

--- SQL JOIN ---


use college;

create table dept(
					department_id int primary key,
                    department_name varchar(50));

insert into dept values
(101,'HR'),
(102,'Finance'),
(103,'IT'),
(104,'Sales');


create table emp(
					employee_id int primary key,
                    employee_name varchar(50),
				    department_id int,
                    salary decimal(10,2));
                    

insert into emp values
(1,'Rahul',101,45000),
(2,'Anu',102,55000),
(3,'John',103,60000),
(4,'Sara',104,52000),
(5,'David',105,48000);





select * from emp
	INNER JOIN dept ON emp.department_id = dept.department_id;
                    
                    
select employee_name,department_name from emp
	inner join dept ON emp.department_id = dept.department_id;
                    



    
--- LEFT JOIN ---
                    
 select employee_name,department_name, salary from  emp e
 left join dept d on e.department_id = d.department_id;
                    
                    
                    

--- RIGHT JOIN ---

 select employee_name,department_name, salary from  emp e
 right join dept d on e.department_id = d.department_id;
                    
                    
                    
--- SELF JOIN ---                 
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    