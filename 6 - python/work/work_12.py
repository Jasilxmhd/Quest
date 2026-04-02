'Python Lab Practical Questions '

'Topic: Sets in Python (Beginner → Advanced) '

'Section 1 – Basic Set Programs '

# 1. Create a set containing 5 numbers and print the set.

# new = { 1, 2, 3 ,4, 5} 
# print(new)

# 2. Create a set with mixed data types and print each element. 

# sample_set = { 'jasil' , 2004 , 10.55 , True, None}
# print(sample_set)

# 3. Write a program to create a set from a list. 

# my_list = [1, 2, 2, 3, 5, 6]

# # convert to set 
# my_set = set(my_list)
# print(my_set)


# 4. Write a program to remove duplicate elements from a list using a set. 


# 5. Create an empty set and add three elements to it.

# sample_Set = set()

# sample_Set.update(['jasil',2004,'Adivaram'])
# print(sample_Set) 

# 6. Write a program to check if an element exists in a set. 
# 7. Create a set and print all elements using a for loop. 

# sample_Set = ('jasil',2004,'Adivaram')
# for i in sample_Set:
#     print(i)


# 8. Write a program to find the length of a set without using len(). 

# s = ( 1 ,2 ,2 ,3 , 4 ,5 )
# count = 0 
# for i in s :
#     count += 1
# print(count)

# 9. Write a program to convert a tuple into a set. 

# t = { 1, 2, 3, 5, "jasil"}
# update = set(t)
# print(update)

# 10. Write a program to convert a set into a list. 

# new_set = {1, 2, 3, 5, 'jasil'}
# convert = list(new_set)
# print(convert)

# 'Section 2  Adding and Removing Elements'

# 11. Create a set and add a new element using add(). 

# new_set = {1, 2, 3, 5, 'jasil'}
# new_set.add('python')
# print(new_set)

# 12. Write a program to add multiple elements to a set using update(). 

# new_set = {1, 2, 3, 5, 'jasil'}
# new_set.update(["pyhton",2004])
# print(new_set)

# 13. Write a program to remove an element using remove(). 
# new_set = {1, 2, 3, 5, 'jasil'}
# new_set.remove("jasil")
# print(new_set)

# 14. Write a program to remove an element using discard(). 

# new_set = {1, 2, 3, 5, 'jasil'}
# new_set.discard("jasil")
# print(new_set)

# 15. Write a program to remove a random element using pop(). 
# new_set = {1, 2, 3, 5, 'jasil'}
# new_set.pop()
# print(new_set)


# 16. Write a program to clear all elements from a set. 

# new_set = {1, 2, 3, 5, 'jasil'}
# new_set.clear()
# print(new_set)

# 17. Write a program to copy a set into another set. 

# new_set = {1, 2, 3, 5, 'jasil'}
# new = new_set.copy()
# print(new)

# 18. Write a program to add elements from a list into a set.

# 19. Write a program to add elements from a tuple into a set. 
# 20. Write a program to update a set with another set. 
 
'Section 3 – Set Operations '

# 21. Write a program to find the union of two sets. 

# s1 = { 1, 2, 3, 4, 5}
# s2 = { 1, 2, 6, 7, 8}

# print(s1 | s2)

# 22. Write a program to find the intersection of two sets. 

# s1 = { 1, 2, 3, 7, 5}
# s2 = { 1, 2, 6, 7, 8}

# print(s1 & s2)

# 23. Write a program to find the difference between two sets. 

# s1 = { 1, 2, 3, 7, 5}
# s2 = { 1, 2, 6, 7, 8}

# print(s1 - s2)

# 24. Write a program to find the symmetric difference between two sets. 

# s1 = { 1, 2, 3, 7, 5}
# s2 = { 1, 2, 6, 7, 8}

# print(s1 ^ s2)

# 25. Write a program to update a set using intersection_update(). 

# s1 = { 1, 2, 3, 7, 5}
# s2 = { 1, 2, 6, 7, 8}

# s2&= s1
# print(s2)

# 26. Write a program to update a set using difference_update(). 

# s1 = { 1, 2, 3, 7, 5}
# s2 = { 1, 2, 6, 7, 8}

# s1.difference_update(s2)
# print(s1)

# 27. Write a program to update a set using symmetric_difference_update(). 

# set1 = { 1,2,3,4,5}
# set2 = { 4,5,6,7,8}

# set1 ^= set2
# print(set1)

# 28. Write a program to check if one set is a subset of another set. 

# s1 = { 1,2,3,4,5}

# s2 = {1}                           
# print(s2.issubset(s1))

# 29. Write a program to check if one set is a superset of another set. 

# s1 = { 1,2,3,4,5}


# s2 = {2,1,5}                       
# print(s1.issuperset(s2))

# 30. Write a program to check if two sets are disjoint. 

set1 = { 1,2,3}
set2 = { 4,5,6}
              

print(set1.isdisjoint(set2))
 
'Section 4 – Logical Set Problems '

# 31. Write a program to find common elements between two lists using sets. 
# 32. Write a program to find unique elements from two lists. 
# 33. Write a program to find elements present in the first list but not in the second list. 
# 34. Write a program to remove duplicates from a sentence using sets. 
# 35. Write a program to find unique characters in a string using sets. 
# 36. Write a program to count unique words in a sentence. 
# 37. Write a program to find the difference between two strings using sets. 
# 38. Write a program to find vowels present in a string using sets. 
# 39. Write a program to check whether two strings contain the same characters. 
# 40. Write a program to find common characters between two strings. 
 
'Section 5 – Set Comprehension '

# 41. Write a program to create a set of squares from numbers 1–10 using set 
# comprehension. 



# 42. Write a program to create a set of cubes using set comprehension. 
# 43. Write a program to create a set of even numbers from 1–20 using set comprehension. 

# even_set = {x for x in range(1, 21) if x % 2 == 0}
# print(even_set)

# 44. Write a program to create a set of odd numbers using set comprehension. 

# numbers = {2, 1, 3, 5, 8, 7, 6}

# odd_numbers = {i for i in numbers if i % 2 != 0}
# print(odd_numbers)

# 45. Write a program to create a set containing lengths of words in a sentence.  
 
'Section 6 – Industry Based Problems '

# 46. Given two sets representing students enrolled in Python and Java, find students 
# enrolled in both courses. 

# python = { 'jasil' , 'niyas' , 'yaseen' }
# java =  { 'niyas' , 'shakir' , 'yaseen' }
# print(python.intersection(java))

# 47. Given two sets representing users who logged in today and yesterday, find new users 
# today. 

# today = { 'user1' , 'user2' , 'user3' , 'user5'}
# yesterday = { 'user1' , 'user4' , 'user2' , 'user6' }

# new = today - yesterday
# print(' New users : ', new)

# 48. Given two sets representing available skills and required job skills, find missing skills.  
# 49. Create a set representing product categories in an e-commerce system and remove a 
# category dynamically. 
# 50. Given two datasets of email IDs, remove duplicates and print all unique email IDs. 
 
'Bonus Interview Questions'

# 1. Why are sets unordered in Python? 
# 2. What is the difference between remove() and discard()? 

'remove'
# person = { 'yaseen', 'jasil', 'niyas', 'shakir'}
# person.remove("jasil")
# print(person)

'discard()'
# person = { 'yaseen', 'jasil', 'niyas', 'shakir'}
# person.discard("jasil")
# print(person)

# 3. Why can't sets contain mutable elements like lists? 
# 4. What is the difference between difference() and difference_update()? 
# 5. When should sets be used instead of lists in real-world applications? 
 