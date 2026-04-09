
# Beginner Level

# • 1. Create a string and print it.
# ch = "Adivaram"
# print(ch)
# • 2. Print each character of a string using indexing.

# ch = "Adivaram"
# for i in range(len(ch)):
#     print(ch[i])

# • 3. Print the first and last character of a string.

# ch = "Adivaram"
# print(ch[0])
# print(ch[-1])

# • 4. Demonstrate positive and negative indexing on a string.
# • 5. Extract the first five characters from a string using slicing.

# s = "python full stack"
# print(s[:5])

# • 6. Reverse a string using slicing.

# s = "python full stack"
# print(s[::-1])

# • 7. Count the length of a string without using len().

# text = "hello world"
# count = 0 
# for i in text :
#     count += 1
# print("Length = ",count)


# • 8. Convert a string to uppercase and lowercase.

# t1 = "MUHAMMED JASIL"
# t2 = "fathima liyaah"
# upper = t2.upper()
# lower = t1.lower()
# print("Upper case = ",upper)
# print("Lower case = ",lower)

# • 9. Capitalize the first letter of a string.

# text = "west way"
# print(text.title())

# • 10. Swap the case of each character in a string.

# text = "Hello World"
# result = text.swapcase()
# print("Swapped case:", result)


# • 11. Check whether a string starts with a specific substring.

# • 12. Check whether a string ends with a specific substring.
# • 13. Count the number of occurrences of a character in a string.
# • 14. Replace a word in a string with another word.
# • 15. Remove leading and trailing spaces from a string.


# Intermediate Level

# • 1. Check whether a string contains only alphabets.

# text = "jasil"
# print(text.isalpha())

# • 2. Check whether a string contains only digits.
# num = "456032"
# print(num.isdigit())

# • 3. Check whether a string is alphanumeric.

# num = "jasil2004"
# print(num.isalnum())

# • 4. Split a sentence into words using split().

# sentence = "Python is easy to learn"
# words = sentence.split()
# print("Words:", words)

# • 5. Join a list of words into a single string.

words = ["Python", "is", "easy", "to", "learn"]

result = " ".join(words)

print("Joined string:", result)

# • 6. Find the first occurrence of a substring in a string.
# • 7. Find the last occurrence of a substring in a string.
# • 8. Remove a prefix from a string.
# • 9. Remove a suffix from a string.
# • 10. Center align a string within a given width.
# • 11. Left justify and right justify a string

text = "Hello"

left = text.ljust(10)
right = text.rjust(10)

print("Left Justified :", left)
print("Right Justified:", right)

# • 12. Pad a number string with zeros using zfill(). 
# • 13. Use format() method in string formatting.
# • 14. Create a formatted string using f-strings.
# • 15. Use partition() to split a string into three parts.



# Logical Problem Solving

# • 1. Check whether a string is a palindrome.
# • 2. Count the number of vowels and consonants in a string.
# • 3. Remove duplicate characters from a string.
# • 4. Find the most frequent character in a string.
# • 5. Check if two strings are anagrams.
# • 6. Reverse each word in a sentence without reversing the sentence order.
# • 7. Find the longest word in a sentence.
# • 8. Compress a string (example: aaabb → a3b2).
# • 9. Remove all spaces from a string.


text = input("Enter a string: ")
result = text.replace(" ", "")
print("String without spaces:", result)

# • 10. Convert the first letter of every word to uppercase without using title().
# • 11. Extract digits from a string and store them separately.
# • 12. Count the number of words in a sentence.
# • 13. Replace multiple spaces with a single space.
# • 14. Check whether a string contains special characters.
# • 15. Find the ASCII value of each character.



# Advanced / Real-world Tasks

# • 1. Encode and decode a string.

# text = "Hello Python"

# # Encode the string
# encoded_text = text.encode()
# print("Encoded:", encoded_text)

# # Decode the string
# decoded_text = encoded_text.decode()
# print("Decoded:", decoded_text)

# • 2. Create a translation table using maketrans() and translate characters.
# • 3. Simulate a simple password validator using string methods.
# • 4. Parse key-value pairs from a string like 'name=John;age=25'.
# • 5. Implement a simple email validation using string methods.
# • 6. Extract hashtags from a text.
# • 7. Mask sensitive data like phone numbers.
# • 8. Implement basic text formatting similar to markdown.
# • 9. Check if a sentence is a pangram.
# • 10. Sort characters in a string alphabetically.
# Interview-Oriented Questions
# • 1. Explain the difference between find() and index() with code.
# • 2. Explain the difference between split() and rsplit() with examples.
# • 3. Explain the difference between strip(), lstrip(), and rstrip().
# • 4. Explain the difference between isdigit(), isnumeric(), and isdecimal().
# • 5. Check whether two strings are rotations of each other.