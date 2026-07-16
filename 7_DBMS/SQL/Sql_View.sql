
use college;
select * from employees;




create view employee_view as
select emp_name,department,salary from employees;

select * from employee_view;


set SQL_SAFE_UPDATES = 0;


update employee_view set emp_name = "kannan" where emp_name = 'rahul sharma';

delete from employee_view where emp_name = 'kannan';







        