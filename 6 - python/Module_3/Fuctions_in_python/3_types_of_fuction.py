
'1. Build in function'
















'2. user defined function'












'3. Recursive function'

# def fact(n):
#     if n ==0:
#         return 1
#     return n* fact(n - 1)

# print(fact(5))







'Stirng reverse'

# def reverse(s):
#     if len(s) == 0:
#         return s
#     return reverse(s[1 : ]) + s [0]

# print(reverse("Jasil Adivaram"))








'4. lambda function'

'square '

# square = lambda a : a**2
# print(square(5))                        # 25
















'sum of 3 number'

# total = lambda a, b, c : a+b+c
# print(total(5,5,5))                                    # 15 















' even aneel square '
' odd aneel cube '

# even_odd = lambda x : x**2 if x % 2 == 0 else x**3
# print(even_odd(10))






'check Length of string'

# str_len = lambda st : len(st)
# print(str_len("jasil"))







'Largest of 2 number'

# large = lambda x,y :f"Largest number is {x}"  if x > y else  f"Largest number is {y}" 
# print(large(10,5))  







'Largest of 3 number'


# large = lambda x,y,z : x if x>y and x>z else( y if y>x and y>z else z)
# print(large(120,300,425))







# large = lambda x, y: f"Both numbers are equal: {x}" if x == y else f"Largest number is {x}" if x > y else f"Largest number is {y}"

# print(large(30, 10))












number = lambda x: f"{x} is a multiple of both" if x % 5 == 0 and x % 3 == 0 else f"{x} is multiple of 3" if x % 3 == 0 else f"{x} is multiple of 5" if x % 5 == 0 else f"{x} is not a multiple of 3 or 5"
print(number(10))

