
-- DDL
use company;
create table emp(
					  emp_name varchar(50),
                      phone_number bigint,
                      salary int not null
);
                      
insert into emp values("Jasil",9746827950,2100);
insert into emp values("Yaseen",12345678,1999),
					("Shakir",9876543210,2750),
                    ("Niyas",6868686868,1500);
                    
select * from emp;

