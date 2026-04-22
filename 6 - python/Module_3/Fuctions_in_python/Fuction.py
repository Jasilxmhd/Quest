
'Fuction'

# def jasil():
#     print('Hello welcome Programmers....')

# # print(type(jasil))                             # <class 'function'>

# jasil()                                          # Hello welcome Programmers....












# def greet(name):
#     print(f' Hello {name} welcome to coding club')

# greet('Jasil')                                         #  Jasil welcome to coding club

















'Argument'

# def add(a,b):
#     print(a + b)

# add(25,25)          # 50















# def add(a , b):
#     return a + b

# result = add(25 , 25)     # data result il store aavunnu 
# print(result)             # 50
 














# def vote(age):
#     if age > 18:
#         return "You are eligibile for voting"
#     else:
#         return "You are eligibile for voting"

# result = vote(25)
# print(result)








'covert to upper case'


# def to_upper(text):
#     return text.upper()

# print(to_upper('jasil'))            # JASIL








'Type Hinting'

# def convert(text : str) -> str :
#     """ This Fuction Convert The Strings to Upper Case"""

#     return text.upper()

# print(convert('jasil'))            # JASIL












def details(name : str , age : int , phone : list) -> str :
    """Get details fro user """
    return name,age,phone

result = details('Jasil',21,[9746827950])
print(result)   