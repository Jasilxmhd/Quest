"""center"""
# s="Python"                       
# print(s.center(25,'*'))          #center align


"""ljust"""
# s="Python"  
# print(s.ljust(25,"⬅"))            #left align


"""rjust"""
# s="Python"  
# print(s.rjust(25,"😁"))           #right align


"""zfill"""
# s="Python"  
# print(s.zfill(9))                 #padd with zeros


"""format"""
name="jasil"                        #format placeholder
age=21 
# print("My name is {} and i am {} year old".format(name,age))        #My name is jasil and i am 21 year old
# print("My name is {} and i am {} year old".format(age,name))        #My name is 21 and i am jasil year old      
# print("My name is {1} and i am {0} year old".format(age,name))      #My name is jasil and i am 21 year old    

# print("My name is {:<10} and i am {} year old".format(name,age))      #My name is jasil     and iam 21 year old    
# print("My name is {:^10} and i am {:05} year old".format(name,age))   #My name is   jasil   and iam 00021 year old 


"""f-string"""
# name="jasil"                        
# age=21 
# print(f"My name is {name} and iam {age} year old") 

"""row-string"""
name="jasil"                        
age=21 
# print(f"My name is {name} \t and iam {age} year old")                  #My name is jasil        and iam 21 year old
# print(r"My name is {name} and iam {age} year old")                     #My name is {name} and iam {age} year old

#Extraaa
# print("''")
# print("""")            # Error
# print("\"\"")            # ""