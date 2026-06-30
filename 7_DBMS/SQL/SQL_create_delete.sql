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



