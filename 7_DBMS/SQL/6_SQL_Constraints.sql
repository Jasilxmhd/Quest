create database bank_db;
use bank_db;

create table accounts (
	accounts_no int not null unique,
    customer_name varchar(50) not null,
    balance decimal(10,2),
    age int not null,
    city varchar(50) default 'calicut'
);


insert into accounts(accounts_no,customer_name,balance,age)values
(2006,'rahul',50000,20);
insert into  accounts(accounts_no,customer_name,balance,age)values
(2099876,'vihan',50000333,22);

select * from accounts;

drop table accounts;