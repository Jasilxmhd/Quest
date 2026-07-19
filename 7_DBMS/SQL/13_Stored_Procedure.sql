


-- Stored Procedure

delimiter //
create procedure show_employees()
	begin 
    select * from employees;
    end //
delimiter ;

call show_employees();














delimiter //
create procedure show_it()
	begin 
    select * from employees where department='it';
    end //
delimiter ;

call show_it();










delimiter //
create procedure count_procedure(out total int)
	begin 
    select count(*) from employees;
    end //
delimiter ;

call count_procedure(@count);
select @count;












delimiter //
create procedure department_details(in dept varchar(500))
	begin 
    select * from employees where  department=dept;
    end //
delimiter ;

call department_details('it');








delimiter //
create procedure addition(in num1 int ,in num2 int)
	begin 
	select num1 + num2 as sum ;
    end //
delimiter ;

call addition(10,20);






delimiter //
create procedure square(inout num1 int)
	begin 
	select pow(num1,2 );
    end //
delimiter ;

set @value = 10;
select @value;

call square(@value);






drop procedure product;



delimiter //
create procedure product(in num1 int,
						in num2 int,
                        out result int)
	begin 
	select num1 + num2 as sum;
    end //
delimiter ;

set @value = 20;
select @value;

call product(10,20,@sum);















