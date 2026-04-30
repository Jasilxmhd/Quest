""" IF-ELSE PRACTICAL QUESTIONS (Beginner Friendly) """

# 1.  Check Even or Odd Write a program to check whether a given number is even or odd.

# num = int(input("Enter a number : "))
# if num % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")



# 2.  Positive, Negative or Zero Write a program to check if a number is positive, negative or zero.

# number = int(input("enter a number : "))
# if number > 0 :
#     print("The number is positive ")
# elif number < 0:
#     print("The number is negative")
# else:
#     print("The number is Zero")




# 3.  Find the Largest of Two Numbers Take two numbers from the user and print the larger one.

# num1 = float(input("Enter a number : "))
# num2 = float(input("Enter another number : "))

# if num1 > num2:
#     print(f"{num1} is a Largest ")
# else:
#     print(f"{num2} is a Largest ")





# 4.  Find the Largest of Three Numbers Take three numbers and print the largest among them.

# num1 = float(input("Enter 1'st number : "))
# num2 = float(input("Enter 2'nd number : "))
# num3 = float(input("Enter 3'rd number : "))

# if num1 > num2 and num1 > num3:
#     print(f"{num1} is a Largest ")
# elif num2 > num1 and num2 > num3:
#     print(f"{num2} is a Largest ")
# else:
#     print(f"{num3} is a Largest")







# 5.  Check Eligibility to Vote Ask the user for their age and check if they are eligible to vote (18 or above).

# age=int(input("Enter tour age :"))

# if age>=18:
#     print("your eligible for vote")
# else:
#     print("your not eligible to vote")








# 6.  Pass or Fail Ask the user for their mark and print Pass if mark is 40 or above, otherwise Fail.


# mark = float(input("Enter a mark : "))
# if mark >=40:
#     print("Pass")
# else:
#     print("Failed")




# 7.  Grade System Input marks and display grade: 90+ : A 80-89 : B 70-79 : C 60-69 : D Below 60 : Fail

# mark = float(input("Enter Your mark number : "))

# if mark >= 90:
#     print("A Grade")
# elif mark >=80:
#     print("B Grade")
# elif mark >=70:
#     print("C Grade")
# elif mark >=60:
#     print("D Grade")
# else:
#     print("Fail")






# 8.  Leap Year Checker Input a year and check whether it is a leap year or not.

# year = int(input("Enter a year : "))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100!=0):
#     print("leap year")
# else:
#     print("not a leap year")






# 9.  Divisible by 5 and 11 Check whether a number is divisible by both 5 and 11.

# num = int(input("Enter a number : "))
# result1 = num % 5 ==0
# result2 = num % 11 ==0
# print("divisable by 5 =",result1)
# print("divisable by 11 =",result2)





# 10. Check Character Type Input a character and check if it is a vowel or consonant.

# alphapet = input("Enter  a one alphapet : ")
# if alphapet in "aeiou":
#     print(f"{alphapet} is vowel")
# else:
#     print(f"{alphapet} is consonent ")








# 11. Simple Login System Ask for username and password. If both are correct, print Login Successful, else Login Failed.

# username = "jasilxmhd"
# password = 'jasil12'

# new_user = input("Please Enter your user Name : ")
# new_pass = input("Please Enter your password : ")

# if username == new_user and password == new_pass :
#     print("Login Successful")
# else:
#     print("Login Failed")






# 12. Number Comparison Game Take two numbers. If first is greater print “First is greater”, else print “Second is greater”.

# num1 = int(input("Enter a first number : "))
# num2 = int(input("Enter a second number : "))

# if num1 > num2 :
#     print("First is greater")
# else:
#     print("Second is greater")






# 13. Check Temperature If temperature > 30 print Hot, if between 20 and 30 print Warm, else Cold.

# temperature = int(input("Enter Temperature : "))
# if temperature > 30 :
#     print("Hot")
# elif temperature >= 20 and temperature <= 30 :
#     print("Warm")
# else:
#     print("Cold")







# 14. Check Salary Bonus If salary > 50000, give bonus 5000 else bonus 2000. Print total salary.

# salary = int(input("Enter your salary : "))
# if salary > 50000 :

#     print(salary + 5000)
# else:
#     print(salary + 2000)






# 15. Check Shopping Discount If bill amount > 1000, give 10% discount else no discount.

# amount=int(input("Enter the bill amount :"))
# if amount > 1000:
#     amount *= 0.90
# print("Last amount :",amount)








# 16. Age Category If age < 13 print Child If age between 13 and 19 print Teen Else print Adult

# age = int(input("Enter your age : "))
# if age < 13 :
#     print("Child")
# elif age >= 13 and age <=19:
#     print("Teen")
# else:
#     print("Adult")








# 17. Electricity Bill Calculator (Simple) If units <= 100 charge 2 per unit If 101-200 charge 3 per unit Above 200 charge 5 per unit

# bill = float(input("Enter your bill amount : "))
# if bill <= 100 :
#     print("2 per unit")
# elif bill >= 100 and bill <=200 :
#     print("3 per unit")
# else:
#     print("5 per unit")








# 18. Check Number is Multiple of 3 or 7 Input a number and check if it is multiple of 3 or 7.

# num = int(input("Enter a number: "))
# if num % 3 == 0 or num % 7 == 0:
#     print(f"{num} is a multiple of 3 or 7")
# else:
#     print(f"{num} is not a multiple of 3 or 7")







# 19. Check Password Strength If password length >= 8 print Strong Password else Weak Password.

# password = input("Enter your password: ")
# if len(password) < 8:
#     print("Password is not strong")
# elif len(password) < 12:
#     print("Password is intermediate")
# else:
#     print("Password is strong")







# 20. Find Smallest of Two Numbers Take two numbers and print the smaller

# num1 = int(input("Enter a first number : "))
# num2 = int(input("Enter a second number : "))
# if num1<num2 :
#     print(f"{num1} is smallest")
# else:
#     print(f"{num2} is smallest")
