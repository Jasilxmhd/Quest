
'vehicle number'

# import re
# with open('regex_practice_dataset.txt','r+')as f:
#     # print(f.read())
#     data = f.read()

#     vehicel_number = re.findall(r'\w{2}-\d{2}-\w{2}-\d{4}',data)
#     print(vehicel_number)






'IP address'

# with open('regex_practice_dataset.txt','r+')as f:
#     # print(f.read())
#     data = f.read()

#     ip = re.findall(r'\d{,3}\.\d{,3}\.\d{,3}\.\d{,2}',data)
#     for i in ip:
#         print(i)
#     print()




'PAN CARD NUMBERS'

# with open('regex_practice_dataset.txt','r+')as f:

#     data = f.read()

#     pan = re.findall(r'[A-Z]{5}\d{4}[A-Z]',data)
#     for i in pan:
#         print(i)
#     print()









# import re

# with open('regex_practice_dataset.txt', 'r') as f:
#     data = f.read()

# emails = re.findall(r'Email: (.*)', data)

# for email in emails:
#     print(email)





s = " jasil muh"
# print(len(s))

word = s.split()
countss = len(word[-1])
print(countss)

