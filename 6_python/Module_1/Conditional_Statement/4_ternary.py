# check even or odd 
# num = int(input("Enter a number : "))
# print("even" if num % 2 ==0 else "odd" )






# Check age
# age = int(input("Enter your age : "))
# status = "Adult" if age >=18 else "Minor"
# print(status)






# num1 = int(input("Enter a number : "))
# num2 = int(input("Enter another number : "))

# print("largest is num" if num1>num2 else "largest number is num 2")




num1 = int(input("Enter 1 st : "))
num2 = int(input("Enter another number : "))
num3 = int(input("Enter a another number : "))

print(f"largest is {num1}" if num1>num2 and num1>num3 else (f"largest is {num2} " if num2>num1 and num2>num3 else f"largest is {num3}" ))
