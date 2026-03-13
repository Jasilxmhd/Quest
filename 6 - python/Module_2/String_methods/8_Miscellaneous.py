"""----------- 6.Miscellaneous -----------"""

"""expandtabs()"""
# print("hello \t python")
# print("hello \t python".expandtabs(10))
# print("hello \t python".expandtabs(23))  
            #syntax:-  [spases=tabsize-(current_position / tabsize)]
# print(len("hello \t python".expandtabs(34)))
# print(len("hello \t python".expandtabs(24)))
# print(len("hello \t python".expandtabs(10)))          


"""translate()"""
# s="yaseen"
# print(s.translate({97:'x',101:'z'}))            #we change the a to x a ascii value is 97 we set 97 to x so the givens strings all a change to x 
#                                                 #yxszzn


# y="hello world"
# print(y.translate({111:"0",108:"!"}))                   #hell0 w0rld
# print(y.translate({111:"0"}))                           #he!!0 w0r!d

# print(chr(111))
# print(ord("!"))
# print(ord("1"))


# s="xxxxyyyyyzzzzz"
# table=s.maketrans('x','z',)                         #zzzzyyyyyzzzzz
# print(s.translate(table))

# s="xxxxyyyyyzzzzz"
# table=s.maketrans('x','z','y')                      #zzzzzzzzz
# print(s.translate(table))


# s="yaseen"
# table=s.maketrans('y','m','en')                     #mas
# print(s.translate(table))


# s="sreeraj"
# table=s.maketrans('sr','xy','e')                     #xyyaj         // s=x and  r=y
# print(s.translate(table))


# s="sreersaj"
# table=s.maketrans('sr','xy','e')                     #xyyxaj         // s=x and  r=y
# print(s.translate(table))


# s="cdalgh"
# table=s.maketrans('abcdefghi','ABCDEFGHI')              #CDAlGH         
# print(s.translate(table))




# split and join
# replase and strip 
# prefix and sufix
# upper ,lower and title
# full in validation and cheking
# index and find
# count