-- DML

create database college;
use college;

create table employee(emp_id int,
					 department varchar(50),
					 salary decimal(10,2),
					 age int,
					 city varchar(50)
);

insert into employee values(101, "developer", 75000,21,"calicut"),
							(102, "Digital marketing", 70000,20,"mukkam"),
							(103, "tester", 62000,20,"wayanad"),
                            (104, "sales", 50000,25,"kochi");

select * from employee;



-- copy the full data of table employee
create table employee_backup as select * from employee;
select * from employee_backup;




-- copy the table skelton of table employee
create table employee_backup1 as select * from employee where 1=0;
select * from employee_backup1;





-- insert a department = " developer " only
insert into employee_backup1 select * from employee where department = "developer";
select * from employee_backup1;









-- UPDATS

update employee set city = "calicut" where emp_id = 102 ;

-- off safe update
SET SQL_SAFE_UPDATES = 0;


select * from employee;

-- update in different columns
update employee set salary = salary + 5000 where city = "calicut";
select * from employee;


update employee set salary = salary + 10, age=18  where city = "calicut";
select * from employee;



 



-- Delete
delete from employee where emp_id = 104 ;
select * from employee;


delete from employee;

insert into employee values(101, "developer", 75000,21,"calicut"),
							(102, "Digital marketing", 70000,20,"mukkam"),
							(103, "tester", 62000,20,"wayanad"),
                            (104, "sales", 50000,25,"kochi"),
                            (105, "sales", 50000,25,"kochi"),
                            (106, "sales", 50000,25,"kochi"),
                            (107, "sales", 50000,25,"kochi"),
                            (108, "sales", 50000,25,"kochi"),
                            (109, "sales", 50000,25,"kochi"),
                            (110, "sales", 50000,25,"kochi");
                            
select * from employee limit 5;                          --  get first 5 datas


select * from employee limit 5 offset 4;                 --  get a 5 data in offset 4 (after 4 datas)


select * from employee limit 5,2;                        -- get data 2 coumns in after 5







 -- -------------------------------------------------------
 
create database colleges;
use colleges;

create table employee (emp_id int,
					  department varchar(50),
					  salary decimal(10,2),
					  age int,
					  city varchar(50)
);

insert into employee values (101, "developer", 75000,21,"calicut"),
							(102, "Digital marketing", 70000,20,"mukkam"),
							(103, "tester", 62000,20,"wayanad"),
                            (104, "sales", 50000,25,"kochi");

select * from employee;

