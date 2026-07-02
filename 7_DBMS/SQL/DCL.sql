-- syntax ----
-- CREATE USER 'username'@'host'
-- IDENTIFIED BY 'password';




 
create user 'jasil'@'localhost'
identified by 'jasil';


select user, host
from mysql.user;



-- GRANT
grant select 
on college.employee
to 'jasil'@'localhost';








grant all privileges
on college.employee
to 'jasilxmhd'@'localhost';


show privileges;










-- REVOKE
revoke select on college.employee
from 'jasil'@'localhost';



show grants for 'jasil'@'localhost';



-- CHANGE USER PASSWORD
alter user 'jasil'@'localhost'identified by 'jasil123'







































