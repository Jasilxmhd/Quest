
use company;
create table employee(
						ID int,
                        Name varchar(30),
                        Salary int
);
Insert into employee values
							(01,"Jasil",28000),
                            (02,"Yaseen",25000);
                            
select * from employee;

start transaction;
update employee
set salary = 35000		
where id = 01		
