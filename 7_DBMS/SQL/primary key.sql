
use college;

create table departments (
	department_id int primary key,
    department_name varchar(50)
);

insert into departments values
(1,'HR'),
(2,'IT'),
(3,'SALES');

select * from departments;

create table student(
id int primary key auto_increment,
s_name varchar(250) not null,
email varchar(75) not null unique,
address varchar(500)not null,
phone_no bigint not null,
d_id int,
foreign key(d_id)
references departments(department_id),

FOREIGN KEY (d_id)
REFERENCES departments(department_id)
ON UPDATE CASCADE
ON DELETE CASCADE
);




describe student;

insert into student values
(100,'Jasil','jasilmuhammed25@gmail','calicut',123456789,2);

insert into student values
(101,'Yaseen','yaseen45@gmail.com','Areekode',6262626262,1),
(102,'Niyas','niyaswyd65@gmail.com','Wayanad',0675067500,3);



select * from student;

update department set department_id = 101 where department_id = 1;

delete from departments where department_name = 'IT';      -- error


show create table student;

alter table student drop foreign key student_ibfk_1;
select * from student;
























































