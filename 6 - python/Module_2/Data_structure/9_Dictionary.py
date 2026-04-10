'Dictionary'

# sample_dictionary = {}
# print(type(sample_dictionary))







# details = { 'Name' : 'Jasil', 'age' : 22 , 'Place' : 'Calicut'}
# print(details)

'Keys'

# # duplicate keys not allowed 
# details = { 'name' : 'Jasil', 'age' : 22 , 'Place' : 'Calicut' , 'name' : 'niyas'}
# print(details)




# # duplicate value are allowed 
# details = { 'name' : 'Jasil', 'surnmae' : 'Jasil' , 'Place' : 'Calicut'}
# print(details)




# sample_dict = { 1 : 'a' , 2 : 'b' , 3 : 'a' , 7.5 :  'd'}
# print(sample_dict)  




# sample_dict = { 1 : 'a' , 2 : 'b' , 3 : 'a' , 7.5 :  'd' , ( 1 , 2 , 2) : 'Tuple'}
# print(sample_dict)


'Set , List , Dictionary not allowed ( key )'









'Values'

## int, float,string, List, Tuple, set, Dictionary

# sample_dict = { 1 : [10,20,30] , 2 : ( 100 , 200 , 'ABC') , 3 : { 40,50, ' Jasil'} , 7.5 :  { 'name' : 'Jasil'} , ( 1 , 2 , 2) : 'Tuple'}
# print(sample_dict)









'Add New Key value in Dictionary '

# student1 = { 'Name' : 'Jasil' , 'Age' : 22}
# print(student1)












'add new key value'

# student1['Place'] = 'Calicut'
# print(student1)













'chenge value only '

# student1['Name'] = 'Niyas'
# print(student1)













'update'

# student1.update({ 'ID' : '007' , 'Domain' : 'React js'})
# print(student1)















'Dictionary ( List case il )'
# student1.update({ 'ID' : '007' , 'Domain' : ['React js']})
# student1['Domain'].append('Jquery')
# print(student1)










'Access Element '

# student1 = { 'Name' : 'Jasil' , 'Age' : 22}

# print(student1['Age'])
# print(student1.get('Name'))

# print(student1.get('place' , 'key doesnt exit'))






'Remove'



'del'
# student1 = { 'Name' : 'Jasil' , 'Age' : 22 , 'rollno' : 250}
# print(student1)

# del student1['rollno']
# print(student1)



'Pop'
# student1 = { 'Name' : 'Jasil' , 'Age' : 22 , 'rollno' : 250}
# student1.pop("Age")
# print(student1)






# student1 = { 'Name' : 'Jasil' , 'Age' : 22 , 'rollno' : 250}
# details = student1.pop("Age")
# print(student1)
# print(details)








'Last key remove cheyyan'

'popitem'

# student1 = { 'Name' : 'Jasil' , 'Age' : 22 , 'rollno' : 250}
# student1.popitem()
# print(student1)






'clear'

# student1 = { 'Name' : 'Jasil' , 'Age' : 22 , 'rollno' : 250}
# student1.clear()
# print(student1)











'For loop '


# student1 = { 'Name' : 'Jasil' , 'Age' : 22 , 'rollno' : 250}

# for key , value in student1.items():
#     print(key,value)




'Print Key onlly'
# student1 = { 'Name' : 'Jasil' , 'Age' : 22 , 'rollno' : 250}

# for key in student1.keys():
#     print(key)




'Print Value onlly'
# student1 = { 'Name' : 'Jasil' , 'Age' : 22 , 'rollno' : 250}

# for value in student1.values():
#     print(value)










# student1 = { 'Name' : 'Jasil' , 'Age' : 22 , 'rollno' : 250}

# print(student1.keys())                      # dict_keys(['Name', 'Age', 'rollno'])
# print(student1.values())                    # dict_values(['Jasil', 22, 250])
# print(student1.items())                     # dict_items([('Name', 'Jasil'), ('Age', 22), ('rollno', 250)])




