#1 Write a program to input two numbers from the user and print their sum.

# num1 = int(input("Enter first num : "))
# num2 = int(input("Enter second num : "))
# total = (num1 + num2)
# print("Sum = ",total)



# 2. Write a program to input two numbers and display( Addition , Subtraction, Multiplication , Division )

# num1 = int(input("Enter first num : "))
# num2 = int(input("Enter second num : "))

# print("a) Addition : ", num1 + num2 ,
#       "b) Subtraction : ", num1 - num2 ,
#       "c) Multiplication ", num1 * num2,
#       "d) Divition ", num1 / num2,
#       )



# 3. Write a program to input two integers and find their product.

# num1 = int(input("Enter first num : "))
# num2 = int(input("Enter second num : "))
# product = num1 * num2
# print("Product : ",product)


# 4. Write a program to input a number and print its square.

# num = int(input("Enter first number : "))
# print("Square is : ",num**2)



# 5. Write a program to input a number and print its cube.
# num = int(input("Enter first number : "))
# print("Square is : ",num**3)


# 6. Write a program to input the length and breadth of a rectangle and calculate its area.

# length = int(input("Enter the lenght  : "))
# width = int(input("Enter the widht  : "))
# area = length * width 
# print("Area of rectangle is : ", area)


# 7. Write a program to input the base and height of a triangle and calculate its area.

# base = float(input("Enter the base : "))
# height = float(input("Enter the height : "))
# area = 0.5 * base * height
# print("Area of triangle = ",area)


# 8. Write a program to input the radius of a circle and calculate its area. (Use π = 3.14)

# radius = float(input("Enter the radius of a circle : "))
# area = 3.14 * radius * radius
# print("Area of the circle = ", area)


# 9. Write a program to input two numbers and find the difference between them.
# num1 = float(input("Enter a first Number : "))
# num2 = float(input("Enter a second Number : "))
# difference = num1 - num2
# print("difference = ",difference)

# 10. Write a program to input two numbers and find the average.
# a = float(input("Enter a first num : "))
# b = float(input("Enter a second num : "))
# average = (a + b) / 2 
# print("Average = ",average)


# =====================
# INTERMEDIATE LEVEL
# =====================

# 11. Write a program to input two numbers and find the remainder using the modulus operator.

# num1 = float(input("Enter a first num : "))
# num2 = float(input("Enter a second num : "))
# remainder = num1 % num2
# print("Remainder = ",remainder)



# 12. Write a program to input two numbers and perform integer division using floor division.

# num1 = float(input("Enter a first num : "))
# num2 = float(input("Enter a second num : "))
# result = num1 // num2
# print("Floor dividsion = ",result)


# 13. Write a program to input a number of days and convert it into:
    # a) Weeks
    # b) Remaining days

# days = int(input("enter number of days : "))
# weeks = days // 7
# remaining_days = days % 7

# print("weeks : ",weeks)
# print("remaining days : ",remaining_days)

# 14. Write a program to input a total amount and number of people, then calculate how much each person should pay.

# total_amount = float(input("enter the total amount : "))
# peoples = float(input("enter the number of people : "))
# each_person = total_amount / peoples
# print("Each person = ",each_person)


"""

17. Write a program to input total seconds and convert it into:
    a) Minutes
    b) Remaining seconds

"""
# seconds = int(input("Enter a seconds : "))
# minute = seconds / 60
# remaining_seconds = seconds % 60

# print("Minute : ",minute)
# print("remaining seconds : ",remaining_seconds)


"""

18. Write a program to input the total marks of 5 subjects and calculate:
    a) Total marks
    b) Average marks

"""
# sub1 = float(input("Enter a sub 1 Mark : "))
# sub2 = float(input("Enter a sub 2 Mark : "))
# sub3 = float(input("Enter a sub 3 Mark : "))
# sub4 = float(input("Enter a sub 4 Mark : "))
# sub5 = float(input("Enter a sub 5 Mark : "))

# total = sub1 + sub2 + sub3 + sub4 + sub5
# average = total / 2

# print("Total Mark : ",total)
# print("Average Mark : ",average)




"""
=====================
LOGIC BUILDING TASKS
=====================

"""
# 21. Write a program to input two numbers and swap them using arithmetic operators (without using a third variable).

# a = 10
# b = 20
# a,b = b,a
# print("a = ",a)
# print("b = ",b)




# 25. Write a program to input a number and calculate the sum of first and last digit.

# digit = int(input("Enter a 3 digit number : "))

# first_num = digit // 100
# last_num = digit % 10 

# addition = first_num + last_num
# print("Sum = ",addition)


num = int(input("Enter table number : "))
limit = int(input("Enter limit : "))
for i in range(1,limit):
    print(f"{limit} x {num} = {limit * num }")
