
'1. Build in function'
















'2. user defined function'












'3. Recursive function'

# def fact(n):
#     if n ==0:
#         return 1
#     return n* fact(n - 1)

# print(fact(5))







# Stirng reverse

# def reverse(s):
#     if len(s) == 0:
#         return s
#     return reverse(s[1 : ]) + s [0]

# print(reverse("Jasil Adivaram"))








'4. lambda function'

# square 

# square = lambda a : a**2
# print(square(5))                        # 25
















# sum of 3 number

# total = lambda a, b, c : a+b+c
# print(total(5,5,5))                                    # 15 














#  even aneel square 
#  odd aneel cube 

# even_odd = lambda x : x**2 if x % 2 == 0 else x**3
# print(even_odd(10))






# check Length of string

# str_len = lambda st : len(st)
# print(str_len("jasil"))







# Largest of 2 number

# large = lambda x,y :f"Largest number is {x}"  if x > y else  f"Largest number is {y}" 
# print(large(10,5))  







# Largest of 3 number


# large = lambda x,y,z : x if x>y and x>z else( y if y>x and y>z else z)
# print(large(120,300,425))







# large = lambda x, y: f"Both numbers are equal: {x}" if x == y else f"Largest number is {x}" if x > y else f"Largest number is {y}"

# print(large(30, 10))












# number = lambda x: f"{x} is a multiple of both" if x % 5 == 0 and x % 3 == 0 else f"{x} is multiple of 3" if x % 3 == 0 else f"{x} is multiple of 5" if x % 5 == 0 else f"{x} is not a multiple of 3 or 5"
# print(number(10))







'5 - Higher order Fuction'

'map fuction '



# def square(nums : int) -> int:
#     return nums ** 2

# numbers = [1,2,3,4,5]



# result = map(square,numbers)
# print(result)                                   # <map object at 0x0000017CD2549A40>



# result = list(map(square,numbers))
# print(result)                                   # [1, 4, 9, 16, 25]









# Another wayy

# result2 = list(map(lambda x : x **2 ,numbers))
# print(result2)                                    # [1, 4, 9, 16, 25]





# print 5 multiplay only

# element = [1,5,10,14,45,35,16,20]

# result  = list(map(lambda x : x % 5 == 0 , element))
# print(result)                                               # [False, True, True, False, True, True, False, True]



# result2 = list(filter(lambda x : x % 5 == 0 , element))
# print(result2)                                              # [5, 10, 45, 35, 20]








# def vowel(word):
#     for ch in word:
#         if ch in 'aeiou':
#             return True
#     return False
    
# name = ['jasil', 'niyas', 'shakir' , 'yaseen']

# r= list(filter(vowel,name))
# print(r)








# sample_list = [0,{},[],5]
# print(any(sample_list))          # True
# print(all(sample_list))          # False











# names = ['jasil','yaseen','shakir','ssssss' ]

# result = list(filter(lambda x : any( ch in 'AEIOUaeiou' for ch in x), names))
# print(result)                                                                    # ['jasil', 'yaseen', 'shakir']







# print only gmail.com and apple.com

# emails = [
#     'jasilmuhammed25@gmail.com',
#     'yaseen256@yaho.com',
#     'shakir456@gmail.com',
#     'niyas123@yahoo.com',
#     'aflah@apple.com'
#     ]

# result = list(filter(lambda x: any(x.endswith(d) for d in ['gmail.com','apple.com']),emails))

# print(result)          # ['jasilmuhammed25@gmail.com', 'shakir456@gmail.com', 'aflah@apple.com']











# 1 - print multiplay of 3 only
# 2 - 3 multiplay to convert cube





# number = [3,6,5,8,9,12,13,9,15]

# result  = list(filter(lambda x : x % 3 == 0 , number))
# print("Multiple of 3 : " , result)                       # Multiple of 3 :  [3, 6, 9, 12, 9, 15]


# result1 = list(map(lambda y : y**3 , result))
# print("Cube :" , result1)                                                    # Cube : [27, 216, 729, 1728, 729, 3375]







number = [3, 6, 5, 8, 9, 12, 13, 9, 15]

result = list(map(lambda x: x ** 3, filter(lambda y: y % 3 == 0, number)))
print(result)                                                                    # [27, 216, 729, 1728, 729, 3375]


