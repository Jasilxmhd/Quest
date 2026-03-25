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

# matrix = [[0,1,2],[3,4,5],[6,7,8]]
# for s in matrix:
#     for m in s:     
#         print(m)



"""append()"""      # Last index il value add cheyyaan

# sample = [1,2,3,4,5,6,7,8,9,100]
# print(dir( sample ))
# sample.append(2004)
# sample.append("Jasil")
# sample.append([200,300,400])

# print(sample)










"""Insert()"""        # add value in specific place

# num = [1,2,3,4,5,6,7,8,9]
# num.insert(1,'jasil')
# print(num)









"""pop()"""            # Remove a element

# num = [1,2,3,4,5,6,7,8,9]
# num.pop()
# print(num)











# remove value in index base 
# num = [1,2,3,4,5,6,7,8,9]
# num.pop(0)
# print(num)










# remove value in neg index 
# num = [1,2,3,4,5,6,7,8,9]
# num.pop(-1)
# print(num)








"""remove()"""
# num = [1,200,3,4,5,6,7,8,9]
# num.remove(200)
# print(num)










'''clear()  '''                      # clear a list ,empty list
# num = [1,200,3,4,5,6,7,8,9]
# num.clear()
# print(num)










'''count()'''                       # count cheyyaan . eg :- 200 ethra thavana undennn
# num = [1,200,3,4,200,5,6,7,8,9]
# print(num.count(200))







'''Copy()'''
# num = [1,200,3,4,5,6,7,8,9,[100,200,7]]
# copy_list = num.copy()


# copy_list[-1][-1]=700
# print(copy_list)                                    # [1, 200, 3, 4, 5, 6, 7, 8, 9, [100, 200, 700]]
# print(num)                                          # [1, 200, 3, 4, 5, 6, 7, 8, 9, [100, 200, 700]]






'''sort()'''                                        # accending order ( 1 2 3 4 5 6 )
# Accesing
# list1 = [1, 200, 9, 7, 5, 0, 3]
# list1.sort()
# print(list1)                                        # [0, 1, 3, 5, 7, 9, 200]

# Deccending
# list1.sort(reverse=True)
# print(list1)                                        # [200, 9, 7, 5, 3, 1, 0]






# Sort in alphabetic order 
# name = ['my', 'name', 'is', 'jasil', 'adivaram']
# name.sort()
# print(name)                                             # ['adivaram', 'is', 'jasil', 'my', 'name']





# Length vechh 
# name = ['myyyyyyyyyyyyy', 'name', 'is', 'jasil', 'adivaram']
# name.sort(key=len)
# print(name)






'''Extend()'''

# list1 = [1, 200, 9, 7, 5, 0, 3]
# list2 = ['jasil',2004,'adivaram']

# list1.extend(list2)
# print(list1)                               # [1, 200, 9, 7, 5, 0, 3, 'jasil', 2004, 'adivaram']



# list1.extend('Muhammed')
# print(list1)                              # [1, 200, 9, 7, 5, 0, 3, 'jasil', 2004, 'adivaram', 'M', 'u', 'h', 'a', 'm', 'm', 'e', 'd']







'''index()'''                                # (value,start,stop)
# list1 = [1, 200, 9, 7, 5, 0, 3]
# print(list1.index(200))                      # 1
# print(list1.index(9,0,3))                    # 2











'''reverse()'''
# list1 = [1, 200, 9,'jasil', 7, 5, 0, 3]
# list1.reverse()
# print(list1)                                # [3, 0, 5, 7, 'jasil', 9, 200, 1]













# list1 = [3, 0, 5, 7, 9, 200, 1]

# # len
# print(len(list1))                                             # 7

# # min
# print(min(list1))                                             # 0

# # max
# print(max(list1))                                             # 200

# # sum
# print(sum(list1))                                             # 225
 
 
# # sorted
# print(sorted(list1))                                          # [0, 1, 3, 5, 7, 9, 200]




# large = 0
# s_large = 0
# nums = [1, 2, 3, 401, 10, 4008, 20]

# for i in range(len(nums)):
#     if nums[i] > large:
#         s_large = large
#         large = nums[i]
#     elif large > nums[i] > s_large:
#         s_large = nums[i]

# print("Largest =", large)
# print("Second Largest =", s_large)








'List Unpacking'

# sample_list = ['apple','banana','mango','grapes']
# x, y, *z = sample_list                                  # * ittaal athikam llath *z kk kayarumm
# print(x)                      # apple
# print(y)                      # banana
# print(z)                      # ['mango', 'grapes']