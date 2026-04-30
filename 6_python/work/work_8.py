# STRING SLICING IN PYTHON – LAB PRACTICAL QUESTIONS

# BASIC LEVEL

# 1.  Write a Python program to take a string from the user and print the
#     first character using slicing.

# ch = input("Enter a string : ")
# print(ch[0])

# 2.  Write a program to display the last character of a string using
#     slicing.

# ch = input("Enter a string : ")
# print(ch[-1])

# 3.  Given a string, print the first 5 characters using slicing.

# ch = input("Enter a string : ")
# print(ch[:5])

# 4.  Write a program to print all characters of a string except the first
#     one.

# ch = "Adivaram"
# print(ch[1::])

# 5.  Write a program to print all characters of a string except the last
#     one.

# ch = "Adivaram"
# print(ch[:-1:])

# 6.  Given a string, print characters from index 2 to index 6.

# ch = "Adivaram"
# print(ch[2:6])

# 7.  Write a program to print every character at even index positions
#     using slicing.

# text = "Python Full Stack"
# result = text[::2]
# print("Even index =  ",result)

# 8.  Write a program to print every character at odd index positions
#     using slicing.

# text = "Python Full Stack"
# result = text[1::2]
# print("Odd index =  ",result)

# 9.  Write a program to reverse a string using slicing.

# text = "Python Full Stack"
# print(text[::-1])

# 10. Given a string, print the middle character(s) using slicing (assume
#     length can be even or odd).


# INTERMEDIATE LEVEL

# 11. Write a program to check whether a string is a palindrome using
#     slicing.

# ch = input("Enter a string ")
# if ch==ch[::-1]:
#     print("padindrom")
# else:
#     print("not a palindrom")

# 12. Given a string, extract the first half and second half using slicing
#     and print them separately.
# name = "Adivaram"
# n=len(name)
# mid =n // 2
# first = name[:mid]
# second = name[mid:]
# print("first half : ",first)
# print("second half : ",second)

# 13. Write a program to remove the first and last two characters from a
#     string using slicing.

# ch = "Adivaram"
# print(ch[1:-2:])



# 14. Given a string, print characters from index 1 to the second last
#     character.

# name ="Adivaram"
# print(name[1:-1:])

# 15. Write a program to extract every third character from a string using
#     slicing.

# 16. Given a string, reverse only the first half of the string using
#     slicing.

# name = "Adivaram "
# n = len(name)
# mid = n // 2 
# first = name[:mid][::-1]
# second = name[mid:]
# print(first,second)

# 17. Write a program to extract the domain name from an email ID using
#     slicing. 





# 18. Given a sentence, extract and print the last word using slicing.

sentence = "Python full stack development"

print(sentence[::])

# 19. Write a program to swap the first and last characters of a string
#     using slicing.

# 20. Given a string, print all characters except vowels using slicing and
#     looping logic.

# 21. Write a program to split a string into two parts based on a given
#     index using slicing.

# 22. Given a string, print the string in reverse order skipping every
#     second character.

# 23. Write a program to extract the username from an email ID using
#     slicing.

# 24. Given a string, check whether the first half and second half are
#     equal using slicing.

# 25. Write a program to count how many characters are present in a
#     substring obtained using slicing.

# CONCEPT-FOCUSED PRACTICE

# 26. Write a program to demonstrate positive and negative indexing using
#     slicing.


# 27. Given a string, show the difference between string[start:end] and
#     string[start:end:step].

# 28. Write a program to demonstrate slicing with only start index, only
#     end index, and only step.

# 29. Write a program to safely slice a string even if the index range
#     exceeds the string length.

# 30. Write a program to show that string slicing does not modify the
#     original string.

# NOTE FOR STUDENTS:

# • Python string slicing format: string[start : end : step] • Start index
# is inclusive, end index is exclusive • Step defines the jump between
# characters • Strings are immutable in Python

