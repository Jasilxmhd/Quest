create database student_db;
use student_db;

create table students (
	student_id int not null unique auto_increment,
    student_name varchar(50) not null,
    email varchar(50),
    address varchar(50) not null,
    phone_no bigint not null
);

insert into students(student_name,email,address,phone_no)values
('rahul','rahul@1223@gmail.com','IRI HO',9037353839);


insert into students(student_name,email,address,phone_no)values
('vinu','vinu@1223@gmail.com','I HO',6737432739);


select * from students;

drop table students;

create table students (
	student_id int primary key,
    student_name varchar(50) not null,
    email varchar(50) not null unique,
    address varchar(50) not null,
    phone_no bigint not null
);

insert into students(student_id,student_name,email,address,phone_no) values(22,'richu','richu.co.in','calicut',90785634121);
insert into students(student_name,email,address,phone_no) values('rinu','rinu.co.in','payyoli',5645342356);
alter table students modify student_id int auto_increment;
select * from students;

drop table students;

create table students (
	student_id int  ,
    student_name varchar(50) not null,
    email varchar(50) ,
    address varchar(50) not null,
    phone_no bigint not null,
    primary key(student_id,email)
);

insert into students(student_id,student_name,email,address,phone_no) values(22,'richu','richu.co.in','calicut',90785634121);

insert into students(student_id,student_name,email,address,phone_no) values(2,'vinu','rinu.co.in','payyoli',5645342356),(32,'sinu','einu.co.in','yoli',5645342356);

select * from students;

describe students;
desc students;

alter table students drop primary key;