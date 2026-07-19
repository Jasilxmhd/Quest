
-- MY SQL FUCTION
-- Numeric Fuctions
select abs(-250);

use college;
select * from employees;

select emp_name,salary, abs(salary - 60000)as salary_difference from employees;







-- celi
select ceil(25.2);       		-- 26

-- floor
select floor(25.2);      		-- 25

-- round
select round(36.5);      		-- 37
select round(35.9);     		-- 36
select round(66.2456,2);  		-- 66.25

select truncate(36.3567,2);  	-- 36.35



-- RANDOM MODULES
select rand();                  -- Rndom number 0-1 . eg :- (0.9346759868177361)


-- Select 2 employees using rand()
select * from employees order by rand() limit 2;



select pow(2,3);      -- 8 (2 Raise to 3)

select sqrt(36);      -- 6 (square root)


select greatest(25,35,20);    -- 35

select emp_name, salary, greatest(salary, 60000)as grestest from employees;


select emp_name, salary, greatest(salary, 60000)as grestest from employees;





select least(25,36,15);    -- 15 

select emp_name, salary, least(salary, 60000)as least from employees;







-- Modules
select mod(25,6);   -- 1 (remainder 25 % 6 = 1 ) 







-- STRING FUNCTION
select ascii('A');   -- 65

select char(65);     -- BLOB

select character_length('jasil');  -- 6

select char_length(emp_name) from employees;

select upper(emp_name) from employees;
select lower(emp_name) from employees;








-- LEFT FUCTION
select emp_name, left(emp_name,5)as First_Five from employees;
select emp_name, right(emp_name,5)as Last_Five from employees;


-- LOCATE
select emp_name, locate('a' , emp_name)as position from employees;   -- get a position of substrign

select emp_name, position('a' in emp_name)as position from employees; 


select emp_name , replace(emp_name,'a','@')as modify_name from employees;




select emp_name , reverse(emp_name)as reverce_name from employees;


-- Concatnate
select concat(emp_name,' - ',department)as employyee_info from employees;
select concat(emp_name,' - ',department,' - ','Calicut')as employyee_info from employees;

select concat_ws(' | ',emp_name,department,'Trackit',city)as emp_info from employees;


-- TRIM
select trim(' Jasil  ')as space from employees;








-- DATE FUNCTION
select date_format(joining_date, '%d -%m -%y')from employees;

select date_format(joining_date, '%D -%M -%Y')from employees;


select current_date();   		-- 2026-07-15
select current_time();   		-- 12:21:39
select current_timestamp();		-- 2026-07-15 12:21:06S



select day(joining_date)from employees;

select dayofyear('2026-07-15');   -- 196
select dayofmonth('2026-07-15');  -- 15
select dayofweek('2026-07-15');   -- 4
select dayname('2026-07-15');     -- Wednesday


































































