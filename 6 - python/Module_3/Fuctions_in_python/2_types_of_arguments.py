'1 positional arguments'




# def details(name : str , age : int , phone : list) -> str :
#     """Get details fro user """
#     return name,age,phone

# result = details(21,'Jasil',[9746827950])
# print(result)                                     # (21, 'Jasil', [9746827950])












'2 Keyword Arguments'

# def details(name : str , age : int , phone : list) -> str :
#     """Get details fro user """
#     print(name)               # Jasil
#     print(age)                # 21
#     print(phone)              # [9746827950]

# details(age=21 , name='Jasil' , phone=[9746827950])













'3 Deafult Argument'

# def add(a , b , c = 2 ):
#     return a+b+c

# print(add(5,5))









'4. Arbitary argument'
 
# def add(*args):

#     total = 0
#     for i in args:
#         total += i
#     return total

# print(add(10,30,50,))









'4. Arbitary Keyword argument'

# def details(**kwargs):
#     print(kwargs)

# details(name = 'jasil' , age = 21)
# details(name = 'jasil' , age = 21 , place = "calicut")
# details(name = 'jasil' , age = 21 , place = "calicut", phn = 9746827950)

















'Access Arbitary Keyword argument'



# def details(**kwargs):
#     for k,v in kwargs.items():
#         print(k,v)

# details(name = 'jasil' , age = 21)
# details(name = 'jasil' , age = 21 , place = "calicut")
# details(name = 'jasil' , age = 21 , place = "calicut", phn = 9746827950)












# def even(*args):
#     for i in args:
#         if i % 2==0:
#             print(i)

# even(1,2,3,4,5,6,7,8,9,10)













# x = 20
# def modify():
#     global x
#     print(x)
#     x = 250

# modify()
# print(x)









# Recursion

# def fact(n):
#     if n ==0:
#         return 1
#     return n* fact(n - 1)

# print(fact(5))







'Stirng reverse'

def reverse(s):
    if len(s) == 0:
        return s
    return reverse(s[1 : ]) + s [0]

print(reverse("Jasil Adivaram"))