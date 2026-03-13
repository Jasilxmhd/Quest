# Python Practical Lab Questions (Logic Building & Interview Prep) 

# Phase 1: Basic Logic & Variable Handling 

# 1. Write a program to swap two variables without using a third (temporary) variable. 

# 2. Create a script that takes a user's name and age as input and prints a message telling them the year they will turn 100. 

# name = input("Enter Your Name : ")
# age = float(input("Enter Your Age : "))
# year = 2026 + (100 - age )
# print(f"{name} you will be 100 years old in {year }")



# 3. Write a program to convert temperature from Celsius to Fahrenheit and vice versa. 




# 4. Calculate the area and perimeter of a rectangle where dimensions are provided by the user. 

# length = float(input("Enter a lenght : "))
# widht = float(input("Enter a width : "))
# area = length * widht
# perimeter = 2 * (length + widht)
# print("Area = ",area)
# print("Perimeter = ",perimeter)



# 5. Write a program to calculate the simple interest based on principal, rate, and time input.

# principle = float(input("Enter a Amount : "))
# rate = float(input("Enter your rate per Annum (%) : "))
# time = float(input("Enter your Duration (year's) : "))

# intrest = principle * (rate * time) / 100
# print("intrest = ",intrest)



# 6. Create a program that takes a character as input and displays its ASCII value. 




 
# 7. Write a script to calculate the distance between two points (x1, y1) and (x2, y2) using the Pythagorean theorem.

# x1 = int(input("Enter X1: "))
# y1 = int(input("Enter Y1: "))
# x2 = int(input("Enter X2: "))
# y2 = int(input("Enter Y2: "))

# distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
# print("Distance =", distance)








# 8. Develop a program that accepts an integer 'n' and computes the value of n + nn + nnn 
# (e.g., if n=5, result is 5 + 55 + 555). 
# 9. Write a program to extract the last digit of a number (e.g., for 1234, the output should be 4). 
# 10. Create a program to find the square root of a number without using the math module (use 
# the exponent operator). 



""" Phase 2: Operators & Conditional Logic """

# 11. Write a program to check if a number is even or odd using the modulo operator. 

# num = int(input("Enter a number : "))
# if num % 2 == 0 :
#     print(f"{num} is a even number ")
# else:
#     print(f"{num} is an odd number ")


# 12. Implement a logic to find the largest of three numbers using nested if-else statements. 

# 13. Write a program to check if a year is a leap year (consider the century year rule). 

# year = int(input("Enter a year : "))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100!=0):
#     print("leap year")
# else:
#     print("not a leap year")

# 14. Create a basic calculator that performs Addition, Subtraction, Multiplication, and Division based on user choice. 

# num1 = float(input("Enter a number : "))
# num2 = float(input("Enter another number : "))

# addition = num1 + num2
# subtraction = num2 - num1
# multiplication = num1 * num2

# print(f"sum = {addition} ")
# print(f"subtraction = {subtraction} ")
# print(f"multiplication = {multiplication} ")


# 15. A student’s grade is determined by their score: 90+ (A), 80-89 (B), 70-79 (C), below 70 (Fail). Write a program using if-elif-else. 

# mark = float(input("Enter Your mark number : "))

# if mark >= 90:
#     print("A Grade")
# elif mark >=80:
#     print("B Grade")
# elif mark >=70:
#     print("C Grade")
# else:
#     print("Fail")



# 16. Write a program to check if a given character is a vowel or a consonant. 
# 17. Implement a "Login System" where the user has 3 attempts to enter the correct password before being locked out. 


# 18. Write a program that checks if a triangle is equilateral, isosceles, or scalene based on its 
# side lengths. 
# 19. Create a script to check if a given number is a multiple of both 5 and 11.

# num1 = int(input("Enter a number : "))
# if num1 %5 == 0 and num1 % 11 == 0:
#     print(f"{num1} is both multiple of 5 and 11 ")
# else:
#     print(f"{num1} is not multiple of 5 and 11 ")





# 20. Use a ternary operator to check if a person is eligible to vote (Age >= 18). 
# age = float(input("Enter your age : "))
# status = "Eligible for voting" if age >=18 else "Not Eligible for voting"
# print(status)

""" Phase 3: Loop Structures (While & For)  """

# 21. Write a program to print the first 10 numbers of the Fibonacci sequence using a while loop. 
# 22. Create a script to find the factorial of a number using a for loop. 
# 23. Write a program to reverse a given integer (e.g., 1234 becomes 4321). 

# num = int(input("Enter a number : "))
# temp = num 
# reverse = 0 
# while temp > 0 :
#     digit = temp % 10 
#     reverse = reverse * 10 + digit
#     temp = temp // 10 
# print(reverse)


# 24. Implement a program to check if a number is a Palindrome (reads the same forward and backward). 

# num = input("Enter a number : ")
# temp = num 
# reverse = 0 
# while temp > 0 :
#     digit = temp % 10 
#     reverse = reverse * 10 + digit
#     temp = temp // 10 
#     print(reverse)

# 25. Write a program to check if a number is a Prime number. 

# limit =int(input("Enter Your limit : "))
# for num in range(2,limit):
#     prime = True
#     for i in range(2,num):
#         if num % i == 0:
#             prime = False
#             break
#     if prime:

# 26. Print all prime numbers between 1 and 100. 

# limit = 100
# for num in range(2,limit):
#     prime = True
#     for i in range(2,num):
#         if num % i == 0:
#             prime = False
#             break
#     if prime:
#         print(num)

# 27. Create a multiplication table (1 to 10) for any number entered by the user. 

# num = int(input("Enter a number : "))
# for number in range(1,11):
#     print(f"{number} x {num} = {number * num }")

# 28. Write a program to find the sum of all digits of a number (e.g., 123 = 1+2+3 = 6). 





# 29. Implement a "Guess the Number" game where the loop continues until the user guesses 
# the correct secret number. 
# 30. Write a program to count the number of vowels in a string provided by the user. 
# Phase 4: Pattern Printing & Nested Loops 
# 31. Print a right-angled triangle pattern of stars (*). 
# 32. Print an inverted right-angled triangle pattern of stars. 
# 33. Print a Pyramid pattern using stars. 
# 34. Print a Diamond pattern using stars. 
# 35. Create a program to print a 5x5 grid of coordinates (e.g., (0,0) (0,1)...). 
# 36. Print a Floyd’s Triangle (consecutive numbers in a triangle format). 
# 37. Use nested loops to find and print all "Armstrong Numbers" between 1 and 500. 
# 38. Write a program to print a Pascal’s Triangle up to 'n' rows. 
# 39. Print a square boundary pattern (stars on the edges, spaces in the middle). 
# 40. Write a script that prints a multiplication table from 1 to 5 using nested loops. 
# Phase 5: Industrial Logic & Optimization (Interview Style) 
# 41. Write a program to find the GCD (Greatest Common Divisor) of two numbers. 
# 42. Implement a script to find the LCM (Least Common Multiple) of two numbers. 
# 43. Create a program that removes all duplicates from a list (without using set()). 
# 44. Write a script to find the second largest number in a list of integers. 
# 45. Implement a "FizzBuzz" program: Print numbers 1-50; for multiples of 3 print "Fizz", for 
# 5 print "Buzz", and for both print "FizzBuzz". 
# 46. Write a program to check if two strings are Anagrams (e.g., "listen" and "silent"). 
# 47. Create a script to find the frequency of each character in a string. 
# 48. Write a program that takes a sentence and reverses each word in its place (e.g., "Hello 
# World" -> "olleH dlroW"). 
# 49. Implement a logic to find the "Perfect Numbers" between 1 and 1000 (a number equal to 
# the sum of its divisors). 
# 50. Write a program to simulate a simple ATM machine: balance inquiry, deposit, and 
# withdrawal (with insufficient balance check). 