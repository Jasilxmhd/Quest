
'Set comprehension'

# numbers = { 2 , 1 , 3 , 5 , 8 , 7 , 6}

# multiple_of_3 = { i for i in numbers if i%3==0 } 
# print(multiple_of_3)








'check Even Or Odd ( Set )'

# numbers = { 2 , 1 , 3 , 5 , 8 , 7 , 6}

# even_or_odd = { 'Even' if num % 2 ==0 else "odd" for num in numbers }
# print(even_or_odd)                                                                # {'Even', 'odd'}



'check Even Or Odd ( List )'

# numbers = { 2 , 1 , 3 , 5 , 8 , 7 , 6}

# even_or_odd = [ 'Even' if num % 2 ==0 else "odd" for num in numbers ]
# print(even_or_odd)                                                                  # ['odd', 'Even', 'odd', 'odd', 'Even', 'odd', 'Even']








# numbers = { 2 , 1 , 3 , 5 , 8 , 7 , 6}

# zero_or_one = { 'zero' if num < 5 else ' one' for num in numbers }
# print(zero_or_one)











numbers = { 2 , 1 , 3 , 5 , 8 , 7 , 6}

zero_or_one = { 'zero' if num < 5 else ' one' if num > 5 else "five"    for num in numbers }
print(zero_or_one)





