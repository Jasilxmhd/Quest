# PYTHON FULL STACK TRAINING: TUPLE LOGIC & INTERVIEW 
# PREP 
# Topic: Tuples, Immutability, and Data Integrity 


#  --- PART 1: BASICS & INITIALIZATION --- 


# 1. Create a tuple containing five different data types (int, float, string, list, boolean). 
# t1 = (10, 7.2, "jasil", [10, 20, 30 ],True)
# print(t1)


# 2. Write a script to check the type of a tuple with a single element. Show the difference 
# t1 = (10, 7.2, "jasil", [10, 20, 30 ],True)
# print(type(t1[2]))
# print(type(t1))

# between (5) and (5,). 
# t1 = (5, )
# t2 = (6)
# print(type(t1))
# print(type(t2))

# 3. Access the last element of a tuple without knowing its length. 
# t1 = (10, 7.2, "jasil", [10, 20, 30 ],True)
# print(t1[-1])

# 4. Access the second to last element of a tuple using negative indexing. 
# t1 = (10, 7.2, "jasil", [10, 20, 30 ],True)
# print(t1[-2])

# 5. Given nested_tuple = ("Python", [10, 20, 30], (5, 15, 25)), print the number 20. 
# nested_tuple = ("Python", [10, 20, 30], (5, 15, 25))
# print(nested_tuple[1][1])


# 6. Check if the element 'Sreeraj' exists in a tuple using a membership operator. 
# t1 = (10, 7.2, "jasil",'Sreeraj', [10, 20, 30 ],True)
# print('Sreeraj' in t1)



# 7. Find the memory size of a list vs. a tuple with the same elements using the sys module. 

# 8. Unpack a tuple of 3 elements into three variables: x, y, and z. 
# person = ('jasil', 'shakir', 'niyas','yaseen')
# x, *y, z = person
# print(x)
# print(y)
# print(z)

# 9. Demonstrate what happens if you try to unpack a tuple of 4 elements into 3 variables. 

# name = ('jasil', 'yaseen', 'shakir','niyas')
# x, *y, z = name
# print(x)
# print(y)
# print(z)







# 10. Use the 'extended iterable unpacking' (using *) to grab the first element and the rest into a 
# list. 













#  --- PART 2: IMMUTABILITY LOGIC --- 
# 11. Write code that attempts to change the first element of a tuple and handle the resulting 
# TypeError gracefully. 
# 12. Given a tuple: t = (1, 2, [3, 4]). Change the value 3 to 30. Explain why this works despite 
# tuples being immutable. 
# 13. Create two tuples, concatenate them, and assign them to a new variable. 
# 14. Use the repetition operator (*) to create a tuple of ten zeros. 
# 15. Swap two variables a and b using tuple unpacking logic in a single line. 
# 16. Write a program to "add" an item to a tuple by converting it to a list first. 
# 17. Write a program to "remove" an item from a tuple. 
# 18. Delete an entire tuple variable from memory and verify its absence using a try-except 
# block. 
# 19. Sort a tuple of integers and return the result as a new tuple. 
# 20. Reverse a tuple using the slicing method [::-1]. 
#  --- PART 3: METHODS & AGGREGATION --- 
# 21. Find the index of the first occurrence of the number 10 in a tuple. 
# 22. Count how many times the string "Python" appears in a tuple of job roles. 
# 23. Find the maximum and minimum values in a tuple of stock prices. 
# 24. Calculate the sum of all numeric elements in a tuple. 
# 25. Given a tuple of tuples: ((1, 2), (3, 4), (5, 6)), calculate the sum of the second element of 
# each internal tuple. 
# 26. Use the index() method to find the position of 'Apple' starting from index 3 in a large fruit 
# tuple. 
# 27. Write a function that takes a tuple and returns a new tuple containing only the even 
# numbers. 
# 28. Convert a list of tuples into a single flat list. 
# 29. Create a tuple from a user-input string where each character is an element. 
# 30. Check if all elements in a tuple are truthy using the all() function. 
#  --- PART 4: SLICING & LOOPING --- 
# 31. Extract a sub-tuple containing the elements from index 2 to 5 (inclusive). 
# 32. Use slicing to get every second element of a tuple. 
# 33. Write a 'for' loop to print each element of a tuple with its corresponding index number. 
# 34. Use a 'while' loop to iterate through a tuple backwards. 
# 35. Create a tuple of 10 numbers and slice it to get the last 3 elements. 
# 36. Slice a tuple to remove the first and last elements. 
# 37. Use a for loop to concatenate all strings in a tuple into a single sentence. 
# 38. Compare two tuples (1, 2, 3) and (1, 2, 4). Explain the logic of how Python compares 
# them. 
# 39. Write a program to find duplicate elements in a tuple. 
# 40. Zip two tuples together to create a list of coordinate pairs.