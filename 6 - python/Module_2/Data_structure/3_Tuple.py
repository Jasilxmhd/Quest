'Tuple'

# t1 = (10, 10.2, 'jasil', [1,2,3,4,5])
# print(t1)
# print(type(t1))







# sample = tuple()
# print(type(sample))








# t2 =  ( 10, )               # comma ( , )  ittal mathree tuple aavullu
# print(type(t2))








# # Length 
# tup = (10, 10.2, 'jasil', [1,2,3,4,5])
# print(len(tup))









# # indexing 
# t5= (10, 10.2, 'jasil', [1,2,3,4,5])
# print(t5[2])







'Add & Update '

# t1 = ( 10, 20, 30 )
# t1 += ( 2004, )
# print(t1)






'Tuple convert to List '
# Tuple entheelum items change cheyyaan List k convert cheyyuka

# t1 = ( 10, 20, 30 )

# sample_list = list(t1)
# sample_list.append(2004)


# # Then List convert to tuple 
# t1 = tuple(sample_list)
# print(t1)





'Tuple Unpacking'

# person = ('jasil','yaseen','shakir','Niyas')
# p1, p2, p3, p4 = person
# print(p1)
# print(p2)
# print(p3)
# print(p4)




# person = ('jasil','yaseen','shakir','Niyas')
# p1, p2, *p3 = person
# print(p1)
# print(p2)
# print(p3)




'Add'
# person = ('jasil','yaseen','shakir','Niyas')
# person = ( *person , 'Liya','Lina')
# print(person)






'delete'   # memmory il ninn thenne delete cheyyan

# person1 = ('jasil','yaseen','shakir','Niyas')
# del person1
# print(person1)










'slice'
# person = ('jasil','yaseen','shakir','Niyas')
# print(person[1])
# print(person[1:])
# print(person[-1])
# print(person[::])









# person = ('jasil','yaseen','shakir','Niyas')
# for p in range(len(person)):
#     print(person[p])










# i = 0
# person = ('jasil','yaseen','shakir','Niyas')
# while i < len(person) :
#     print(person[i])
#     i += 1










'Tuple inbuilt methods '
# person = ('jasil','yaseen','shakir','Niyas')
# # print(dir(person))
# print(person.count('yaseen'))
# print(person.count('aju'))










# index 
# person = ('jasil','yaseen','shakir','Niyas')
# print(person.index('jasil'))
# print(person.index('Niyas'))













# membership 
# person = ('jasil','yaseen','shakir','Niyas')
# print('jasil' in person)
# print('aju' in person)













# *
# person = ('jasil','yaseen','shakir','Niyas')
# print(person * 3)







