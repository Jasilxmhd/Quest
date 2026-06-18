'Ramdom Modules'


# Random number pick cheyyan

from random import *
# print(random())
                                              

# print(randint(0,500))      # start,stop
# print(randrange(0,8,2))    # start,stop,step













'choice'

# students =['jasil','shakir','yaseen','niyas']
# print(choice(students))                                       # shakir






# name ="muhammed"
# print(choice(name))                                         # u











'choices'

# students =['jasil','shakir','yaseen','niyas']

# print(choices(students,k=3))                                # ['yaseen', 'shakir', 'jasil']









# name = 'muhammed'
# print(choices(name,k=3))                                         # ['m', 'e', 'e']












'shuffle'           # only list

# students =['jasil','shakir','yaseen','niyas']
# shuffle(students)
# print(students)












'sample'

# students =['jasil','shakir','yaseen','niyas']

# print(sample(students,k=3))                                 # ['jasil', 'yaseen', 'shakir']



















'uniform'

# value = uniform(0,5)
# print(value)                                      # 2.3328297142858374

# rounded_value=round(value,2)
# print(rounded_value)                              # 2.33








'Simple Guss game'

# value = randint(0,10)
# user = int(input('Guss a number (1-9) : '))
# if user==value:
#     print("Your win !")
# else:
#     print("Your Fail")

# print('Random num :',value)









# value = randint(0,100)
# user = int(input('Guss a number (1-99) : '))

# if value < user:
#     print("number Too low")
# elif value > user:
#     print("To High")
# else:
#     print("congrats your Win !!")

# print(value)











'Head or tail'

# result = choice(['Head','Tail'])
# print(f'congrats the Result is : {result}')








'question picker'

# question = ['whats is python','Features of pythom','Current version of python']
# print(choice(question))                                                             # Features of pythom
















'OTP'

# from random import*

# num = randint(1,999999)
# otp = f'{num:06d}'
# print(f'OTP : {otp}')                          # OTP : 544007










