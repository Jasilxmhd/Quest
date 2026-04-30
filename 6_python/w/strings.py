
# string reverse 
# name = input("Enter a name : ")
# reverse = " "
# for char in name:
#     reverse = char + reverse
# print(reverse)


# swap

# a = "quest"
# b = "calicut"

# a,b=b,a

# print(a)
# print(b)




# palindrom

# ch = input("Enter a string ")
# if ch==ch[::-1]:
#     print("padindrom")
# else:
#     print("not a palindrom")




# check anagram 

# word1 = input("Enter a string : ")
# word2 = input("Enter a another word : ")
# if sorted(word1.lower())== sorted(word2.lower()):
#     print("anagram")
# else:
#     print("not an anagram")






# frequancy 
# ch = "hello world"
# for i in range(len(ch)):
#     count = 0 
#     for j in range(len(ch)):
#         if ch[i] == ch[j]:
#             count += 1
    # print(ch[i], ":",count)






# from collections import Counter
# ch = "hello world"
# print(Counter(ch))







# repeting character
# text = "Programming"
# for i in text:
#     if text.count(i) > 1 :
#         print(i)




# text = "Programming"
# for i in text:
#     if text.count(i) == 1 :
#         print("first non repeating : ", i )
#         break





text = input("Enter a word: ")
result = ""

for ch in text:
    if ch not in result:
        result = result + ch

print(" removing duplicate:", result)

