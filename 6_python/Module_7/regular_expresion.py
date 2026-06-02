
'Regular Expresion'



'\d'

'Search'

# import re

# data = 'My Phone NUmber is 9746827950'
# pattern = r'\d\d\d'

# result = re.search(pattern, data)
# print(result.group())






'Findall'

# import re

# data = 'My 100 Phone NUmber is 9746827950'
# pattern = r'\d\d'

# # result = re.search(pattern, data)
# result1 = re.findall(pattern, data)

# # print(result.group())
# print(result1)







'match'    '(Beginnig onlyy)'

# import re

# data = '456789 My Phone NUmber is 9746827950'
# pattern = r'\d\d\d'

# # result = re.search(pattern, data)
# result1 = re.match(pattern, data)

# # print(result.group())
# print(result1.group())




'..................................................'



'\D'   ' (Any charactor . that is not a digit)'



# import re

# data = 'My 100 Phone Number @ 🎶 is 9746827950'
# pattern = r'\D\D'

# result = re.findall(pattern, data)


# print(result)






'\w' '( Any alpaha numeric character + Underscore)'

# import re

# data = 'My 100 Phone Number @ _ \n 🎶 is 9746827950'
# pattern = r'\w'

# result = re.findall(pattern, data)


# print(result)





"\W"  '( Any character Not alpha numeric (symbols , spaces))'

# import re

# data = 'My 100 Phone Number @ _ \n 🎶 is 9746827950'
# pattern = r'\W'

# result = re.findall(pattern, data)


# print(result)








'\s' '(Any white spaces(space, tap, newline))'


# import re

# data = 'My 100 Phone Number @ _ \n 🎶 is 9746827950'
# pattern = r'\s'

# result = re.findall(pattern, data)


# print(result)






'\S'

# import re

# data = 'My 100 Phone Number @ _ \n 🎶 is 9746827950'
# pattern = r'\S'

# result = re.findall(pattern, data)


# print(result)






' . (dot)'

# import re

# data = 'My 100 Phone Number @ _ \n 🎶 is 9746827950'
# pattern = r'.'

# result = re.findall(pattern, data)


# print(result)







'............................................'







# import re

# data = 'My 100 Phone Number @ _ \n 🎶 is 9746827950'
# pattern = r'9........0'

# result = re.findall(pattern, data)


# print(result)


'................................................'



import re

data = 'My Phone NUmber is +91 97468 27950 or +91 96561 77550'

pattern = r'\+91 \d{5} \d{5}'

result = re.findall(pattern, data)
print(result)
