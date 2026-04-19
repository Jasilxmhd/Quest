'PYTHON FULL STACK TRAINING: DICTIONARY LOGIC & INTERVIEW PREP '

'Topic: Key-Value Pairs, JSON-like Structures, and Data Mapping --- PART 1: DICTIONARY BASICS & CREATION --- '



# 1. Create a dictionary representing a 'Laptop' with keys: brand, model, and price. 

# Laptop = {'brands' : 'mac' , 'model' : 'M4' , 'price' : '94,990'}
# print(Laptop)

# 2. Access the value of the 'model' key using square brackets. 

# Laptop = {'brands' : 'mac' , 'model' : 'M4' , 'price' : '94,990'}
# print(Laptop['model'])

# 3. Access the value of a key that doesn't exist using .get() and explain why it's safer than []. 
# 4. Create an empty dictionary using both {} and the dict() constructor. 
# 5. Add a new key-value pair 'processor': 'i7' to an existing dictionary. 

# Laptop = {'brands' : 'mac' , 'model' : 'M4' , 'price' : '94,990'}
# Laptop['processor'] = ' i7 '
# print(Laptop)

# 6. Update the 'price' of the laptop to a new value. 

# Laptop = {'brands' : 'mac' , 'model' : 'M4' , 'price' : '94,990'}
# Laptop['price'] = '95,000'
# print(Laptop)


# 7. Use the len() function to find how many key-value pairs are in a dictionary. 

# Laptop = {'brands' : 'mac' , 'model' : 'M4' , 'price' : '94,990'}
# print(len(Laptop))

# 8. Create a dictionary where the keys are numbers 1 to 5 and the values are their squares. 

# sqaure = {}
# for i in range(1,6):
#     sqaure[i] = i*i
# print(sqaure)

# 9. Check if a specific key exists in a dictionary using the 'in' operator. 
# 10. Delete a key-value pair using the 'del' keyword and handle the case if the key is missing.


' --- PART 2: METHODS & MANIPULATION --- '

# 11. Use the pop() method to remove a key and store its value in a variable. 

# Laptop = {'brands' : 'mac' , 'model' : 'M4' , 'price' : '94,990'}
# Laptop.pop('brands')
# print(Laptop)

# 12. Use popitem() to remove the last inserted item and explain its behavior in Python 3.7+.

# Laptop = {'brands' : 'mac' , 'model' : 'M4' , 'price' : '94,990'}
# Laptop.popitem()
# print(Laptop)


# 13. Use the keys() method to print all the keys in a dictionary. 

# Laptop = {'brands' : 'mac' , 'model' : 'M4' , 'price' : '94,990'}
# print(Laptop.keys())


# 14. Use the values() method to print all the values in a dictionary. 

# Laptop = {'brands' : 'mac' , 'model' : 'M4' , 'price' : '94,990'}
# print(Laptop.values())



# 15. Use the items() method to iterate through a dictionary and print "Key: Value" for each pair. 

# Laptop = {'brands' : 'mac' , 'model' : 'M4' , 'price' : '94,990'}
# print(Laptop.items())


 
# 16. Merge two dictionaries: {'a': 1, 'b': 2} and {'c': 3, 'd': 4} using the update() method. 

# a = {'a': 1, 'b': 2}
# b = {'c': 3, 'd': 4}

# c = a
# c.update(b)
# print(c)

# 17. Clear all items from a dictionary using the clear() method. 

# Laptop = {'brands' : 'mac' , 'model' : 'M4' , 'price' : '94,990'}
# print(Laptop.clear())

# 18. Use the setdefault() method to add a key 'country' with value 'India' only if it doesn't exist. 

# Laptop = {'brands' : 'mac' , 'model' : 'M4' , 'price' : '94,990'}

# result = Laptop.setdefault('country', 'India')
# print(Laptop)



# 19. Create a shallow copy of a dictionary and show that modifying the copy doesn't change 
# the original. 
# 20. Create a dictionary from two lists: one for keys and one for values using the zip() function. 

# a = { 1 , 2 , 3 }
# b = { 10 , 20 , 30 }

# c = dict(zip(a , b))
# print(c)

'--- PART 3: NESTED DICTIONARIES (API STYLE) --- '

# 21. Create a nested dictionary called 'Employees' containing data for three different people. 

# Employees = {
#     'emp1' : {
#         'Name'        : 'Jasil',
#         'Age'         : 21,
#         'Department'  : 'IT'

#     },
#     'emp2' : {
#         'Name'        : 'Niyas',
#         'Age'         :  20,
#         'Department'  :  'Designing'

#     },
#     'emp3'  : {
#         'Name'        : 'Yaseen',
#         'Age'         : 21,
#         'Department'  : 'Finance'
#     }
# }

# print(Employees)


# 22. Access a value inside a nested dictionary (e.g., Employees['emp1']['salary']). 

# Employees = {
#     'emp1' : {
#         'Name'        : 'Jasil',
#         'Age'         : 21,
#         'Salary'      : '3.5 LPA',
#         'Department'  : 'IT'

#     },
#     'emp2' : {
#         'Name'        : 'Niyas',
#         'Age'         :  20,
#         'Salary'      : '4 LPA',
#         'Department'  : 'Designing'

#     },
#     'emp3'  : {
#         'Name'        : 'Yaseen',
#         'Age'         : 21,
#         'Salary'      : '5 LPA',
#         'Department'  : 'Finance'
#     }
# }

# print(Employees['emp1']['Salary'])




# 23. Update a value inside a nested dictionary. 

# Employees = {
#     'emp1' : {
#         'Name'        : 'Jasil',
#         'Age'         : 21,
#         'Salary'      : '3.5 LPA',
#         'Department'  : 'IT'

#     },
#     'emp2' : {
#         'Name'        : 'Niyas',
#         'Age'         :  20,
#         'Salary'      : '4 LPA',
#         'Department'  : 'Designing'

#     },
#     'emp3'  : {
#         'Name'        : 'Yaseen',
#         'Age'         : 21,
#         'Salary'      : '5 LPA',
#         'Department'  : 'Finance'
#     }
# }

# Employees['emp2']['Name']='Shakir'
# print(Employees['emp2'])


# 24. Add a new nested dictionary (a new employee) to the existing 'Employees' structure. 

# Employees = {
#     'emp1' : {
#         'Name'        : 'Jasil',
#         'Age'         : 21,
#         'Salary'      : '3.5 LPA',
#         'Department'  : 'IT'

#     }

# }



# Employees.update(
#     {
#         'emp2' : {
#             'Name' : 'Aljith',
#             'Age'  : 21,
#         }
#     }
# )

# print(Employees)


# 25. Write a loop to print only the names of all employees from the nested 'Employees' dictionary. 


# Employees = {
#     'emp1' : {
#         'Name'        : 'Jasil',
#         'Age'         : 21,
#         'Salary'      : '3.5 LPA',
#         'Department'  : 'IT'

#     },
#     'emp2' : {
#         'Name'        : 'Niyas',
#         'Age'         :  20,
#         'Salary'      : '4 LPA',
#         'Department'  : 'Designing'

#     },
#     'emp3'  : {
#         'Name'        : 'Yaseen',
#         'Age'         : 21,
#         'Salary'      : '5 LPA',
#         'Department'  : 'Finance'
#     }
# }

# for emp in Employees:
#     print(Employees[emp]['Name'])


# 26. Create a dictionary where a key points to a list of values (e.g., 'hobbies': ['coding', 
# 'reading']). 

person = {
    'name': 'Jasil',
    'age': 21,
    'hobbies': ['coding', 'reading', 'gaming']
}

print(person)

# 27. Append a new hobby to the list inside that dictionary. 

# Dictionary with a list
person = {
    'name': 'Jasil',
    'hobbies': ['coding', 'reading']
}

# Append a new hobby
person['hobbies'].append('gaming')

# Print result
print(person)

# 28. Given a dictionary of students and their marks (a list), calculate the average marks for one 
# student. 
# 29. Flatten a simple nested dictionary (convert {'a': {'b': 1}} to {('a', 'b'): 1}). 
# 30. Represent a JSON response from a weather API as a nested dictionary and extract the temperature



'--- PART 4: COMPREHENSIONS & LOGIC ---'


# 31. [Comprehension] Create a dictionary of even numbers between 1-10 as keys and their cubes as values.

even_cubes = {x: x**3 for x in range(1, 11) if x % 2 == 0}
print(even_cubes) 

# 32. [Comprehension] Given a dictionary, create a new one with only items where the value is 
# > 100. 
# 33. [Comprehension] Swap keys and values in a dictionary (Reverse Mapping). 
# 34. Sort a dictionary by its keys in alphabetical order. 


data = {
    'banana': 3,
    'apple': 5,
    'cherry': 2
}


sorted_dict = dict(sorted(data.items()))

print(sorted_dict)

# 35. Sort a dictionary by its values in ascending order. 
# 36. Find the key with the maximum value in a dictionary of product prices. 

# 37. Count the frequency of each character in a string "Python Trainer" using a dictionary. 

# 38. Combine two dictionaries by adding values for common keys. 
# 39. Convert a dictionary into a list of tuples. 
# 40. Check if all values in a dictionary are the same. --- PART 5: INDUSTRIAL & INTERVIEW SCENARIOS --- 
# 41. [JSON] Use the 'json' module to convert a dictionary into a JSON string. 
# 42. [Data Cleaning] Remove all keys from a dictionary that have None or empty string 
# values. 
# 43. [Security] Explain why a list cannot be used as a dictionary key, but a tuple can. 
# 44. [Logic] Write a program to find the sum of all values in a numeric dictionary. 
# 45. [Simulation] Use a dictionary to simulate a simple "Switch-Case" statement logic. 
# 46. [Efficiency] Compare the time it takes to find a value in a list of 10,000 items vs. a 
# dictionary. 
# 47. [Functionality] Use **kwargs in a function to accept arbitrary keyword arguments as a 
# dictionary. 
# 48. [Mapping] Create a dictionary to map Roman numerals to Integers (e.g., 'I': 1, 'V': 5). 
# 49. [Logic] Given a list of words, group them by their starting letter using a dictionary. 
# 50. [Interview Question] Explain the difference between '==' and 'is' when comparing two 
# identical dictionaries. 