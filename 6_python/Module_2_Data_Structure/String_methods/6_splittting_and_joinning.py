
"""split()"""
# s="welcone to the world of python"                 #split a string      //output is a list   
# print(s.split())                                   #['welcone', 'to', 'the', 'world', 'of', 'python']
# print(s.split(" ",3))                              #['welcone', 'to', 'the', 'world of python']

# s="welcone-to-the-world-of-python"                
# print(s.split("-"))                                #same as above
# print(s.split("-",3))                              #['welcone', 'to', 'the', 'world-of-python']

# print("hello".split("l"))                          #['he', '', 'o']
# print("helllo".split("l"))                         #['he', '', '', 'o']


"""rsplit()"""                                      #split left to righr
# s="welcone to the world of python"                #split a string      //output is a list   
# print(s.rsplit(" ",3))                            #['welcone to the', 'world', 'of', 'python']


"""join()"""                                      #split left to righr
# s="welcone to the world of python"  

# split=s.split()                                   #Split the the words
# print(split)                                      #'welcone', 'to', 'the', 'world', 'of', 'python']


# jointed_string=" ".join(split)                    #join splited list the the words
# print(jointed_string)                             #welcone to the world of python

# print(" ".join(split))


"""partition()"""
# s="job = python"
# print(s.partition("="))                           #('job ', '=', ' python')


# s="job=python"
# print(s.partition("python"))                      #('job ', '=', ' python')

# s="python"
# print(s.partition("python"))                      #('', 'python', '')
# s="python"
# print(s.partition("x"))                           #('python', '', '')


# s="my name is yaseen"
# print(s.partition(" "))                           #('my', ' ', 'name is yaseen')


"""rpartition()"""
# s="my name is yaseen"
# print(s.rpartition(" "))                            #('my name is', ' ', 'yaseen')