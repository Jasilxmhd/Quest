# List 

# details = ['Jasil',21,'Calicut']
# print(details)




# sample_list = []
# print(type(sample_list))




# sample_list2 = list()
# print(type(sample_list2))





# sample = [1,2,3,'Jasil',10.25,[10,20,30],True,None]
# print(sample)





# list1 = list('Jasil')                 # ['J', 'a', 's', 'i', 'l']
# list1 = list([1,2,3])                 # [1, 2, 3]
# list1 = list(1)     
#                   # Error                              
# print(list1)





# Access in a List Element 

# address = [1,2,3,'Jasil',[0,6,7,5],True]

# print(address[3])                           # Jasil
# print(address[5])                           # True







"""List Operation """
# add

# numbers = [1,2,3,4,5,6,7,8,9]
# numbers += [10]
# print(numbers)


# numbers += 'jasil'
# print(numbers)




# 2 List add cheyyan 

# list1 = [1,2,3,4,5,6,7,8,9]

# list2 = [10,20,30,40,50,60]


# update_list = list1 +list2
# print(update_list)                                   # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50, 60]








# Repatition

# num = [1,2,3,4,5,6,7,8,9]
# num *= 10
# print(num)




# Accessing 
# num = [1,2,3,4,5,6,7,8,9]
# print(num[3])                               # 4




# Update
# num = [1,2,3,4,5,6,7,8,9]
# num[3] = 400
# print(num)                                    # [1, 2, 3, 400, 5, 6, 7, 8, 9]




# sum 
# num = [1,2,3,4,5,6,7,8,9]
# num[3] += 400
# print(num)                                      # [1, 2, 3, 404, 5, 6, 7, 8, 9]



# Membership operator 

# num = [101,2,3,4,500,6,7,8,9,[10,20]]
# print(500 in num)                                  # True
# print(20 in num [9])                               # True

# print(len(num[9]))                                 # 2





"""Indexing""" 

# num = [101,2,3,4,500,6,7,8,9,[10,20]]
# print(num[4])                                         # 500
# print(num[9])                                         # [10, 20]
# print(num[10])                                        # Error

# print(num[-6])                                        # 500
# print(num[9][0])                                      # 10





# num = [101,'jasil',2,3,4,500,6,7,8,9,[10,20]]
# print(num[1][2])                                        # s










'''List Slicing '''

# num = [101,'jasil','Niyas',2,3,4,500,6,7,8,9,[10,20,30]]
# print(num[1 : 3])                                               # ['jasil', 'Niyas']
# print(num[: : 2])                                               # [101, 'Niyas', 3, 500, 7, 9]
# print(num[3 : ])                                                # [2, 3, 4, 500, 6, 7, 8, 9, [10, 20 , 30]]
# print(num[3 : -1 ])                                             # [2, 3, 4, 500, 6, 7, 8, 9]
# print(num[: -1 ])                                               # [101, 'jasil', 'Niyas', 2, 3, 4, 500, 6, 7, 8, 9]
# print(num[: : -1 ])                                             # [[10, 20], 9, 8, 7, 6, 500, 4, 3, 2, 'Niyas', 'jasil', 101]
# print(num[-1 : 7 : -1 ])                                        # [[10, 20 , 30], 9, 8, 7]
# print(num[1][1:4])                                              # asi
# print(num[-1][1:])                                              # [20, 30]







# Matrix 

matrix = [[0,1,2],[3,4,5],[6,7,8]]
for s in matrix:
    for m in s:     
        print(m)








