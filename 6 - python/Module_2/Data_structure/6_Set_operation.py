'Set Operation'


'1 - Union ()'



# set1 = { 1,2,3,4,5}
# set2 = { 4,5,6,7,8}

# print(set1.union(set2))
# print(set1 | set2)







# set1 = { 1,2,3,4,5}
# set2 = { 4,5,6,7,8}
# set3 = { 7,8,9,22}

# print(set1.union(set2,set3))
# print(set1 | set2 |set3)








# sample = { 1,2,3,4,5,5,6,4 }
# print(len(sample))








# python = { 'najad' ,  'jasil' , 'yaseen' , 'shakir' }
# django = { 'shahal' ,  'jasil' , 'yaseen' , 'shakir' , 'niyas' }

# print(python | django)                                               # python or django










'2 - intersection ()'

# set1 = { 1,2,3,4,5}
# set2 = { 4,5,6,7,8}

# print(set1.intersection(set2))






# set1 = { 1,2,8,4,5}
# set2 = { 4,5,6,7,8}
# set3 = { 4,5,9,71,8}

# print(set1.intersection(set2,set3))
# print(set1 & set2 & set3)












# python = { 'najad' ,  'jasil' , 'yaseen' , 'shakir' }
# django = { 'shahal' ,  'jasil' , 'yaseen' , 'shakir' , 'niyas' }

# ## print(python.intersection(django))
# print(python & django)                                                          # python and django














# python = { 'najad' ,  'jasil' , 'yaseen' , 'shakir' }
# django = { 'shahal' ,  'jasil' , 'yaseen' , 'shakir' , 'niyas' }

# result = python & django
# print(result)
# print(python)








'InterSection update'

# set1 = { 1,2,8,4,5}
# set2 = { 4,5,6,7,8}

# set2.intersection_update(set1)
# set2&= set1

# print(set2)






# set1 = { 1,2,8,4,5}
# set2 = { 4,5,6,7,8}

# set2.intersection_update(set2)
# print(set2)








'Difference'

# set1 = { 1,2,8,4,5}
# set2 = { 4,5,6,7,8}

# print(set1.difference(set2))
# print(set1 - set2)

# print(set2 - set1)

# print(set2 - set2)                                      # set()



# set1.difference_update(set2)
# print(set1)





'Symmetric Difference'

# set1 = { 1,2,3,4,5}
# set2 = { 4,5,6,7,8}

# print(set1.symmetric_difference(set2))
# print(set1 ^ set2)








'Symmetric Difference Update'

set1 = { 1,2,3,4,5}
set2 = { 4,5,6,7,8}

set1.symmetric_difference_update(set2)
set1 ^= set2
print(set1)






