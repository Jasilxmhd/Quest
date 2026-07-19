create database Quest;
use Quest;

show tables;


create table student(id int, s_name varchar(50), address text);

select * from student;

insert into student(id, s_name, address) values(101, "Jasil", "Adivaram");
insert into student(id, s_name, address) values(102, "Yaseen", "Areekode");
insert into student(id, s_name, address) values(103, "Shakir", "Vadakara");
insert into student values(104, "Niyas", "Wayanad"); 							 -- Ella column thkkum add cheyyan column name kodkkanda

insert into student(s_name) values("Ibrahim");

select id,s_name from student; 													 -- id um name maaathram show cheyyan

select * from student where id = 101;       									 -- id 101 get a full details

insert into student values(104, "Shahal", "Calicut"),(105, "Arshad", "Koduvally"),(106, "Rajin", "Mukkam"); -- multiple values add cheyyan
select * from student;


truncate student;                                                                  --   delete entire table



drop table student;                                  --  remove table
drop database quest;                                 --  remove database



-- ALTER

alter table student add salary decimal(10,2);      --  add new column salary (add)

alter table student modify s_name varchar(80);     -- data type changing (modify)
select * from student;

alter table student rename column id to s_id;      -- column name changing
select * from student;



-- Alter 
create database company;
use company;

create table employee (id int, name varchar(50), age int);

insert into employee values(101, "Jasil", 21),(102, "Arshad", 24),(103, "Rajin", 20);
select * from employee;

alter table employee add email varchar(50) first;                 -- add email column first

-- Create new column specific position
alter table employee add phone varchar(50) after name;         --  add phone column after name


-- Create new column and set default value
alter table employee add department varchar(50) default "IT";	

-- Delete a column
alter table employee drop column email;


-- Rename Table Name
alter table employee rename to staff;
select * from staff;
