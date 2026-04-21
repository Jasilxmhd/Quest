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

def add(a , b , c = 2 ):
    return a+b+c

print(add(5,5))