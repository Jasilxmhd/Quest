

'........ Compile Function ........'

# import re
# data = '10 h a a5  My name is jasil .2004  I am from Adivaram . My phone number is 9746827950 ✅'

# pattern = r'\d+'
# number = re.compile(pattern)   # Compile


# result = number.findall(data)
# print(result)





'........ Sub Function ........'


# import re
# data = '10 h a a5  My name is jasil .2004  I am from Adivaram . My phone number is 9746827950 ✅'

# # Replace cheyyan ( ITh original na effect cheyyola)
# new_data = re.sub(r' ','💕', data, count=3)  # Count used to ethra vattam replace cheyyan
# print(new_data)                     # 10💕h💕a💕a5  My name is jasil .2004  I am from Adivaram . My phone number is 9746827950 ✅







'........ Subn Function ........'


# import re
# data = '10 h a a5  My name is jasil .2004  I am from Adivaram . My phone number is 9746827950 ✅'

# update_data = re.subn(r' ','💕', data, count=3) 
# print(update_data)                               # ('10💕h💕a💕a5  My name is jasil .2004  I am from Adivaram . My phone number is 9746827950 ✅', 3)








'........ split Function ........'


import re
data = 'My name is jasiele .2004  I am from Adivaram . My phone number is 9746827950 ✅'

# splited_data = re.split(r'e', data)  # e ullath okka split aaavum
splited_dataa = re.split(r'e',data,  maxsplit=3)  # maxsplit ethra vattam . count poole

# print(splited_data)       # ['My nam', ' is jasil .2004  I am from Adivaram . My phon', ' numb', 'r is 9746827950 ✅']  
print(splited_dataa)        # ['My nam', ' is jasi', 'l', ' .2004  I am from Adivaram . My phone number is 9746827950 ✅']         

