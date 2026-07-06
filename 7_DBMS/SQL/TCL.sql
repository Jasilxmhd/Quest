

-- TCL (Transaction Control Language)
create database bank_db;
use bank_db;

create table accounts (
	account_no int primary key,
    customer_name varchar(50),
    balance decimal(10,2)
);

insert into accounts values
	(1001,"Jasil",50000),
	(1002,"Yaseen",55000),
	(1003,"Rajin",40000),
	(1004,"Niyas",49000);

select * from accounts;


start transaction;                                                     --  start transaction; begin;

update accounts set balance = balance + 500
where account_no = 1001;

select * from accounts;

commit;







begin;

update accounts set balance = balance + 1000
where account_no = 1002;

select * from accounts;

rollback;









begin;

insert into accounts values (1005,"Kabeer",75500);
savepoint bonus;                                         --  create savepoint

insert into accounts values (1006,"Hadhi",64300);
savepoint bonus1;

insert into accounts values (1007,"Haris",81000);

select * from accounts;

rollback to bonus;
rollback to bonus1;                         -- call savepoint

release savepoint bonus;                    --  remove savepoint
release savepoint * ;                       --  remove all savepoints

commit;                                     -- close transation




-- ---------------------------------------------------


drop table accounts;

create table accounts (
	account_no int not null unique,
    customer_name varchar(50) not null,
    balance decimal(10,2) not null
);

insert into accounts values (2000,'Jasil',50000);
insert into accounts values (2001,null,50000);
insert into accounts values (2002,'Yaseen',null);

select * from accounts;














