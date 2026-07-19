
CREATE DATABASE work; 
USE work;

CREATE TABLE books ( 
					book_id INT PRIMARY KEY AUTO_INCREMENT,
                    title VARCHAR(100), author VARCHAR(100),
                    category VARCHAR(50),
                    publisher VARCHAR(100),
                    price DECIMAL(8,2),
                    quantity INT,
                    language VARCHAR(30),
                    publish_year INT
); 


INSERT INTO books (
					title, author, category, publisher, price, quantity, language, publish_year)
                    VALUES 
                    ('Python Basics','John Smith','Programming','TechPress',650,15,'English',2022),
                    ('Learning SQL','David Lee','Database','TechPress',700,12,'English',2021),
                    ('Java Complete','James Brown','Programming','CodeWorld',850,8,'English',2020),
                    ('C Programming','Dennis Hall','Programming','CodeWorld',500,20,'English',2019),
                    ('HTML & CSS','Emily Clark','Web','BrightBooks',450,18,'English',2023), 
                    ('JavaScript Guide','Alex Roy','Web','BrightBooks',600,10,'English',2022),
                    ('Data Science','Sophia White','Data Science','AI Publications',950,7,'English',2024),
                    ('Machine Learning','Andrew Green','Data Science','AI Publications',1200,5,'English',2023),
                    ('Deep Learning','Andrew Green','Data Science','AI Publications',1300,4,'English',2024),
                    ('PHP Essentials','Mark David','Programming','TechPress',550,14,'English',2021),
                    ('MySQL Guide','David Lee','Database','TechPress',680,9,'English',2023),
                    ('Networking Basics','Kevin John','Networking','NetBooks',750,6,'English',2022),
                    ('Linux Commands','John Smith','Operating System','TechPress',500,11,'English',2020),
                    ('Cyber Security','Kevin John','Security','NetBooks',900,7,'English',2024),
                    ('Cloud Computing','Emily Clark','Cloud','BrightBooks',1100,5,'English',2023);

select * from books;
	
    
    
-- Display all books ordered by title in ascending order. 
select * from books order by title asc;


-- Display all books ordered by price in descending order.
select * from books order by price desc;


-- Display the title, category, and price ordered by category. 
select title,category,price from books order by title,category,price;


-- Display all books ordered by publish year (latest first). 
select * from books order by publish_year desc;


-- Display all books sorted by publisher and then by price (highest first). 
select * from books order by price desc;



-- Display books ordered by quantity from lowest to highest.
select title,quantity from books order by quantity asc;



-- Display books published after 2021, ordered by price.
select * from books where publish_year>2021 order by price asc;



-- Display all Programming books ordered by title.



-- Display books ordered by author name and then title. 
select title,author from books order by title asc , author;


-- Display all books ordered by category and publish year. 
select * from books order by category , publish_year;









-- Count the number of books in each category. 
select category , count(*) as Each_Category from books group by category;




-- Find the average price of books in each category.
select category , avg(price) from books group by category;




-- Find the highest-priced book in each category. 





-- Lowest price in each publisher
SELECT publisher, MIN(price) AS lowest_price FROM books GROUP BY publisher;



-- Total quantity available in each category
select category,sum(quantity) as Total_Quantity from books group by category;




-- 6. Count books by each publisher
select publisher , count(*) as book_count from books group by publisher;



-- 7. Average quantity for each publisher
select publisher,avg(quantity) as AVG_Quantity from books group by publisher;



-- Total book value in each category
select category, sum(quantity * price) as Total_Value from books group by category;



-- Latest publish year in each category
select category , max(publish_year) as Latest_yr from books group by category;


-- Display categories having more than 2 books. 
select category,count(*)as book_count from books group by category having count(*)>2;



 -- Display publishers whose average book price is greater than 700.
 
 select publisher, avg(price)as avarage_pricce from books group by publisher having avg(price)>700;
 
 
 
 
-- Display categories where the total quantity is greater than 20. 
select category, sum(quantity) as T_Quantity from books group by category having sum(quantity)>20;
 
 
 
 
 
 -- Display publishers whose total number of books is at least 3. 
 select publisher, count(*)as quantii from books group by publisher having count(*) >= 3;
 
 
 
 
 --- Part E – GROUP BY + HAVING + ORDER BY  
 
 -- Display categories with an average price greater than 600, ordered by average price in descending order. 
 select category, avg(price)as AVG_PRICE from books group by category having avg(price)>600 order by AVG_PRICE desc;
 

 
 
 -- Display publishers having more than 2 books, ordered by total books in descending order.
 select publisher ,count(*)as count_ from books group by publisher having count(*)>2 order by count_ desc;
 
 
 
 
 -- Display authors whose average book price is greater than 700, ordered by average price.
 select author,avg(price)as book_price from books group by author having avg(price)>700 order by book_price asc;
 
 
 
 
 -- Display categories whose total quantity is greater than 15, ordered alphabetically.
 select category , sum(quantity)as t_quantuty from books group by category having sum(quantity) > 15 order by t_quantuty asc;
 
 
 
 
 -- Display publishers whose total stock value (price × quantity) is greater than 10000, ordered from highest to lowest. 
 select publisher , sum(price * quantity) as total_stock from books group by publisher having sum(price * quantity) > 10000 order by total_stock asc;
 
  
 select * from books;