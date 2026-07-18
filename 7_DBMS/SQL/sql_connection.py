
import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Jasil@2004",
    database = "college"
)

if connection.is_connected():
    print("Connected Successfully")


cursor = connection.cursor()

# cursor.execute("select * from employees")
cursor.execute("select salary,city from employees")
result = cursor.fetchall()
print(result)