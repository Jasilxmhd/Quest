# Python Data Structures (Lists) – Lab Practical
# Question Bank
# Beginner → Advanced + Logical & Interview-Oriented Questions
# Section 1: Beginner Level

# 1 1. Create a list of five integers and print all elements using a for loop.

# L1 = [ 10, 21, 203]
# for i in L1:
#     print(i)

    
# 2 2. Write a program to find the length of a list without using len().
# L1 = [ 10, 21, 203]
# count = 0 
# for i in L1:
#     count += 1
# print(count)

# 3 3. Create a list of numbers and print the maximum and minimum values.

# L1 = [ 10, 21, 203, 2004]
# print(max(L1))
# print(min(L1))


# 4 4. Write a program to append a new element to a list entered by the user.

# L1 = [ 10, 21, 203, 2004]
# print(L1)
# update =input("Please Enter : ")
# L1.append(update)
# print(L1)

# 5 5. Insert an element at a specific position in a list.

# L1 = [ 10, 21, 203, 2004]
# L1.insert(1,"Adivaram")
# print(L1)

# 6 6. Remove an element from a list using remove() and pop().

# L1 = [ 10, 21, 203, 2004]
# # pop
# L1.pop(1)
# print(L1)

# Remove
# L2 = [ 10, 21, 203, 2004]
# L2.remove(2004)
# print(L2)

# 7 7. Write a program to check whether a given element exists in a list.

# L1 = [ 10, 21, 203, 2004]
# print( 2004 in L1)

# 8 8. Reverse a list without using reverse().

# L1 = [ 10, 21, 203, 2004]
# print(L1[::-1])


# 9 9. Sort a list of numbers in ascending and descending order.

# ascending
# L1 = [ 100, 21, 5, 2004]
# L1.sort()
# print(L1)

# # descending
# L1.sort(reverse=True)
# print(L1)

# 10 10. Create a list of numbers and print only the even numbers.

# num = [ 0, 2, 4, 5, 7]
# new_list = [n for n in num if n %2==0]
# print(new_list)



# 11. Count how many times a specific element appears in a list.

# num = [ 0, 2, 4, 5, 7,7]
# print(num.count(7))

# 12. Write a program to copy one list into another list.

# num = [ 0, 2, 4, 5, 7,7]
# copy_list = num.copy()
# print(copy_list)

# 13. Concatenate two lists using the + operator.

# num = [ 0, 2, 4, 5, 7,7]
# num1 = [ 1, 2, 3, 4, 5, 6]

# new_list = num + num1
# print(new_list)


# 14. Repeat a list three times using the * operator.
# num = [ 1, 2, 3, 4, 5, 6]
# print(num * 3 )


# 15. Demonstrate positive and negative indexing in a list.
# num = [ 1, 2, 3, 4, 5, 6]
# print(num[0])     # positive
# print(num[-6])    # Negative


'Section 2: Intermediate Level'

# 1 16. Write a program to remove duplicates from a list.

# num = [ 1, 2, 3, 4, 5, 6, 6]
# new_list = set(num)

# update = list(new_list)
# print(update)



# 2 17. Find the second largest element in a list.

# num = [ 1, 2, 3, 4, 5, 6, 6] 


# 3 18. Write a program to rotate a list to the left by one position.
# 4 19. Write a program to rotate a list to the right by one position.
# 5 20. Move a specific element (e.g., 50) to the first position of a list.
# 6 21. Create a list of squares of numbers from 1–10 using list comprehension.
# 7 22. Create a list containing only odd numbers from 1–50 using list comprehension.
# 8 23. Write a program to merge two lists and remove duplicates.
# 9 24. Find the sum of all elements in a list without using sum().
# 10 25. Write a program to find common elements between two lists.
# 11 26. Write a program to split a list into two halves.
# 12 27. Find the index of a given element without using index().
# 13 28. Write a program to flatten a nested list.
# 14 29. Create a program to find the frequency of each element in a list.
# 15 30. Reverse each element of a list of strings.

'Section 3: Advanced Level'

# 1 31. Implement a matrix using nested lists and print it in matrix format.
# 2 32. Write a program to add two matrices using nested lists.
# 3 33. Write a program to transpose a matrix.
# 4 34. Flatten a 2D list into a single list using list comprehension.
# 5 35. Find the largest sublist length in a nested list.
# 6 36. Write a program to find the intersection of multiple lists.
# 7 37. Write a program to group list elements by their length (strings).
# 8 38. Implement a simple stack using a Python list.
# 9 39. Implement a queue using a Python list.
# 10 40. Write a program to shuffle elements in a list.
# 11 41. Write a program to find the kth largest element in a list.
# 12 42. Write a program to check whether a list is a palindrome.
# 13 43. Write a program to generate all possible pairs from a list.
# 14 44. Create a list of prime numbers within a given range using list comprehension.
# 15 45. Write a program to remove all negative numbers from a list.

'Section 4: Logical / Problem Solving'

# 1 46. Given a list of numbers, move all zeros to the end while maintaining order.
# 2 47. Find the first non-repeating element in a list.
# 3 48. Find the highest frequency element in a list.
# 4 49. Find all pairs whose sum equals a given target value.
# 5 50. Write a program to detect duplicates in a list.
# 6 51. Given two lists, determine whether they contain the same elements regardless of order.
# 7 52. Write a program to partition a list into even and odd numbers.
# 8 53. Implement bubble sort using lists.
# 9 54. Implement selection sort using lists.
# 10 55. Write a program to remove consecutive duplicate elements.

'Section 5: Interview-Oriented Questions'

# 1 56. Explain the difference between list.copy() and copy.deepcopy(). Demonstrate with code.
# 2 57. What is list comprehension? Write examples and compare it with loops.

# number = [i for i in range(1,11)]  
# print(number) 


# 3 58. What happens when you modify a list during iteration? Demonstrate with an example.
# 4 59. Explain the difference between append(), extend(), and insert().


# append()
# sample = [1,2,3,4,5,6,7,8,9,100]
# sample.append("Jasil")
# print(sample)



# insert()
# num = [1,2,3,4,5,6,7,8,9]
# num.insert(1,'jasil')
# print(num)

# extend()
# num = [1,2,3]
# num.extend([4, 5])
# print(num)



# 5 60. Demonstrate shallow copy behavior using lists.
# 6 61. Explain time complexity of list operations (append, insert, pop).
# 7 62. Write a program to implement a stack using a list and explain push/pop.
# 8 63. Write a program to remove duplicates while preserving order.
# 9 64. Explain the difference between mutable and immutable data structures in Python.
# 10 65. Write a Python program to simulate a simple task queue using lists.