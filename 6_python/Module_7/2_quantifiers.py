
'Quantifiers'

# import re

# data = 'My name is jasil . I am from Adivaram . My phone number is 9746827950'

# result = re.search(r'jasil', data)
# print(result)                         # <re.Match object; span=(11, 16), match='jasil'>
# print(result.group())                 # jasil



# 'Search Inbuild Methods'

# print(result.start())                 # 11               ( starting index)
# print(result.end())                   # 16               ( ending index)
# print(result.span())                  # (11, 16)






# import re

# data = 'My name is jasil . I am from Adivaram . My phone number is 9746827950'

# result = re.findall(r'\d{10}', data)
# print(result)                          # ['9746827950']









# import re

# data = 'My name is jasil . I am from Adivaram . My phone number is 9746827950'

# result = re.findall(r'\w{2}', data)    # 2 vech group cheyyamn

# print(result)      # ['My', 'na', 'me', 'is', 'ja', 'si', 'am', 'fr', 'om', 'Ad', 'iv', 'ar', 'am', 'My', 'ph', 'on', 'nu', 'mb', 'er', 'is', '97', '46', '82', '79', '50']












# import re

# data = 'h a My name is jasil . I am from Adivaram . My phone number is 9746827950'

# result = re.findall(r'\w{2,}', data)    # minimum 2 

# print(result)   # ['My', 'name', 'is', 'jasil', 'am', 'from', 'Adivaram', 'My', 'phone', 'number', 'is', '9746827950']







# import re

# data = 'h a My name is jasil . I am from Adivaram . My phone number is 9746827950'

# result = re.findall(r'\w{2,5}', data)    # minimum 2 maximum 5

# print(result)   # ['My', 'name', 'is', 'jasil', 'am', 'from', 'Adiva', 'ram', 'My', 'phone', 'numbe', 'is', '97468', '27950']











# import re

# data = 'h a My name is jasil . I am from Adivaram . My phone number is 9746827950'

# result = re.findall(r'\S{2,5}', data)

# print(result)      # ['My', 'name', 'is', 'jasil', 'am', 'from', 'Adiva', 'ram', 'My', 'phone', 'numbe', 'is', '97468', '27950']





# import re

# data = 'h a My name is jasil . I am from Adivaram . My phone number is 9746827950'
# print(len(data))                      # 73

# result = re.findall(r'\d{,5}', data)
# print(len(result))                    # 66
# print(result)                         # ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '97468', '27950', '']










# import re

# data = 'h a 5  My name is jasil .2004  I am from Adivaram . My phone number is 9746827950'

# result = re.findall(r'\d+', data)   # Atlast one

# print(result)                       # ['5', '2004', '9746827950']






'+'

# import re

# data = 'h a a5  My name is jasil .2004  I am from Adivaram . My phone number is 9746827950'

# result = re.findall(r'\w+', data)    # Atlear one word

# print(result)    # ['h', 'a', 'a5', 'My', 'name', 'is', 'jasil', '2004', 'I', 'am', 'from', 'Adivaram', 'My', 'phone', 'number', 'is', '9746827950']





# import re

# data = 'h a a5  My name is jasil .2004  I am from Adivaram . My phone number is 9746827950'

# result = re.findall(r'\w*', data)    # zero or more

# print(result)          # ['h', '', 'a', '', 'a5', '', '', 'My', '', 'name', '', 'is', '', 'jasil', '', '', '2004', '', '', 'I', '', 'am', '', 'from', '', 'Adivaram', '', '', '', 'My', '', 'phone', '', 'number', '', 'is', '', '9746827950', '']









# import re

# data = 'h a a5  My name is jasil .2004  I am from Adivaram . My phone number is 9746827950'

# result = re.findall(r'\w\w?', data)    # zero or 

# print(result)   # ['h', 'a', 'a5', 'My', 'na', 'me', 'is', 'ja', 'si', 'l', '20', '04', 'I', 'am', 'fr', 'om', 'Ad', 'iv', 'ar', 'am', 'My', 'ph', 'on', 'e', 'nu', 'mb', 'er', 'is', '97', '46', '82', '79', '50']













'........................................................'


import re

test_case = 'a ab abc abbc abbcc abbbccc abbbbcccc'
result = re.findall(r'a\w*', test_case)
result1 = re.findall(r'a\w+', test_case)
result2 = re.findall(r'a\w?', test_case)
print(result)                                     #  ['a', 'ab', 'abc', 'abbc', 'abbcc', 'abbbccc', 'abbbbcccc']
print(result1)                                    #  ['ab', 'abc', 'abbc', 'abbcc', 'abbbccc', 'abbbbcccc']
print(result2)                                    #  ['a', 'ab', 'ab', 'ab', 'ab', 'ab', 'ab']
