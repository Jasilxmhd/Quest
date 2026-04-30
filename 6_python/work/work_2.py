""" I. Arithmetic & Assignment Operators (1-15) """

# 1. Write a program to calculate the area and perimeter of a rectangle.

# length = float(input("Enter a length : ")) 
# width = float(input("Enter a width : ")) 

# area = length * width
# perimeter = (length + width)* 2

# print("The Area of rectangle = ", area )
# print("The Perimeter of rectangle = ",perimeter )



# 2. Given a total number of days, convert it into years, weeks, and days.

# total = int(input("Enter a number of days : "))

# year = total / 365
# week = total / 7
# day = total / 1

# print("Year = ",year)
# print("week = ",week)
# print("Day = ",day)



# 3. Calculate the compound interest for a given principal, rate, and time. 

# principle = float(input("Enter a Amount : "))
# rate = float(input("Enter your rate per Annum (%) : "))
# time = float(input("Enter your Duration (year's) : "))

# intrest = principle * (rate * time) / 100
# print("compund intrest = ",intrest)



# 4. Write a program to swap two variables using only arithmetic operators ($+$ and $-$). 

# a = 10
# b = 5

# a = a+b
# a = 15 - 10
# b = 15 - 5

# print("A = ",a)
# print("B = ",b)



# 5. Demonstrate the difference between / (float division) and // (floor division) using positive and negative numbers. 
# a = int(input("Enter a Dividend : "))
# b = int(input("Enter a Divisor : "))

# float_division = a / b
# floor_division = a // b 

# print("Float Division = ",float_division)
# print("Floor Division = ",floor_division)



# 6. Find the remainder of $12345$ divided by $67$ using the modulo operator. 

# a = 12345
# b = 67
# modules = a % b 
# print("The remainder is  = ",modules)



# 7. Write a script to calculate $a^b$ without using the pow() function. 
# num = int(input("Enter a num : "))
# num1 = int(input("Enter a num : "))
# power = num ** num1 
# print("The power of a number is :",power)



# 8. Create a simple "Tip Calculator": Input bill amount and percentage, output the final total.

# amount = int(input("Enter the bill amount : "))
# percentage = float(input("Enter a percentage : "))
# tip_amount = amount * percentage/100
# Total = amount - tip_amount
# print("The final amount is : ",Total)



# 9. Use the += operator to keep a running total of 5 user-input numbers. 

# num1 = int(input("Enter a 1st number : "))
# result = 0
# result += num1
# num2 = int(input("Enter a 2nd number : "))
# result += num2
# num3 = int(input("Enter a 3rd number : "))
# result += num3
# num4 = int(input("Enter a 4th number : "))
# result += num4
# num5 = int(input("Enter a 5th number : "))
# result += num5
# print("Totall = ",result)






# 10. Given a 3-digit number, find the sum of its digits using / and %. 

# digit = int(input("Enter a 3 digit number : "))

# first_num = digit // 100
# second_num = (digit // 10) % 10
# last_num = digit % 10 

# addition = first_num + second_num + last_num
# print("Sum = ",addition)






# 11. Write a program to convert Celsius to Fahrenheit: $F = (C \times 9/5) + 32$. 
# Celsius = int(input("Enter a Celsius : "))
# Fahrenheit = (Celsius * 1.8) + 32
# print("Fahrenheit is : ", Fahrenheit)





# 12. Calculate the surface area of a sphere given its radius. 

# radius = float(input("Enter the radius: "))
# area = 4 * 3.14 * radius * radius
# print("Surface Area of Sphere =", area)





# 13. Implement a program that calculates the BMI (Body Mass Index) based on weight (kg) and height (m). 

# weight = float(input("Please Enter your weight (kg) : "))
# height = float(input("Please Enter your height (m) : "))

# height_square = height ** 2
# total = weight / height_square

# print("The BMI is : ",total)





# 14. Show how the * operator behaves differently with integers vs. strings. 
# num = int(input("Enter a num : "))
# sum = num * num
# print("Result = ",sum)

# words = input("Enter a word : ")
# result = words * 3
# print("Result = ",result)






''' II. Relational & Comparison Operators (16-25) '''

# 16. Write a program to check if a user-input number is even or odd. 
# num = int(input("Enter a number : "))
# if num % 2==0:
#     print("The number is even")
# else:
#     print("The number is odd")







# 18. Check if a given year is a leap year using comparison and logical operators. 

# year = int(input("Enter a year : "))
# if (year % 400 == 0) or (year % 4 == 0 and year % 100!=0):
#     print("leap year")
# else:
#     print("not a leap year")




# 19. Take two numbers and print True if the first is greater than the second, else False. 

# num1 = float(input("Enter a number : "))
# num2 = float(input("Enter another number : "))

# if num1 > num2:
#     print("True")
# else:
#     print("False ")






# 20. Determine if a student passed or failed based on a passing mark of 40. 

# mark = float(input("Enter a mark : "))
# if mark >=40:
#     print("Pass")
# else:
#     print("Failed")




# 21. Compare a float and an integer (e.g., 5.0 == 5). Explain the result. 
# num1 = int(input("Enter a integer number : "))
# num2 = float(input("Enter a float number : "))

# result = num1 == num2
# print(result)




# 23. Write a program to find the largest of three numbers using comparison operators. 

# num1 = float(input("Enter a 1st number : "))
# num2 = float(input("Enter a 2nd number : "))
# num3 = float(input("Enter a 3rd number : "))

# if num1 >= num2 and num1 >= num3:
#     print(f"The Largest Number is : {num1}")
# elif num2 >= num1 and num2 >= num3:
#     print(f"The Largest Number is : {num2}")
# else:
#     print(f"The Largest Number is : {num3}")




""" III. Logical Operators (26-35) """


# 26. Check if a number is divisible by both 3 and 5.
# num = int(input("Enter a number : "))
# result1 = num % 5 ==0
# result2 = num % 3 ==0
# print("divisable by 5 =",result1)
# print("divisable by 3 =",result2)






# 27. Write a program to check if a number is between 10 and 50 (inclusive). 

# num = float(input("Enter a number: "))

# if 10 <= num <= 50:
#     print("The number is between 10 and 50 inclusive .")
# else:
#     print("The number is NOT between 10 and 50.")





# 30. Determine if a person is eligible to vote (Age $\ge 18$ AND has a Voter ID). 

# age = float(input("Enter a your age : "))
# if age >= 18 :
#     print("you are eligible for Voting")
# else:
#     print("you are Not eligible for Voting ! ")





# 31. Check if a number is either positive OR even. 

# number = int(input("enter a number : "))
# if number > 0 :
#     if number % 2 ==0:
#         print(f"{number} is both positive and even")
#     else:
#         print(f"{number} is both positive and not a even")
# else:
#     print(f"{number} is negative")




# 33. Write a program that checks if a character is a vowel using the or operator. 

# alphabet = input("Enter one alphabet: ")

# if alphabet == "a" or alphabet == "e" or alphabet == "i" or alphabet == "o" or alphabet == "u":
#     print(f"{alphabet} is a vowel")
# else:
#     print(f"{alphabet} is a consonant")





# 34. Check if a number is NOT divisible by 7.

# num=int(input("Enter a number :"))
# if not(num%7==0):
#     print(f"{num} is not divisible by 7")
# else:
#     print(f"{num} is  divisible by 7")




""" V. Intermediate Logic Building (46-50) """

# 46. The Range Checker: Take a number and check if it’s outside the range 100-200.

# num = float(input("Enter a number : "))
# if num <= 100 and num >=200 :
#     print(f"{num} is outside the range ")
# else:
#     print(f"{num} is inside the range ")




# 49. Shopping Discount: Apply a 10% discount using *= only if the total is above $500. 

# amount=int(input("Enter the bill amount :"))
# if amount>500:
#     amount *= 0.90
# print("Last amount :",amount)