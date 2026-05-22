
'Polymorphism'


""" 



                        -------  Overloading (Compile time Polymorphsm)
                        -
 Polymorphism (2 types) -
                        -
                        -------  Overriding (Run time Polymorphsm)                          
        


        
        
"""



# class Animal:

#     def speak(self):
#         pass


# class Dog(Animal):

#     def speak(self):
#         print("Bow Bow")






'----------------------------------------------------------------------------------'






"""




                        -------  Operation Overloading
                        -
                        -
 OverLoading (3 types)  -------  Method OverLoading ( Python not support )
                        -
                        -
                        -------  Constructor OverLoading  ( Python not support in directly )
                        



                        
 """







'Operator OverLoading'



# class Operation:

#     def add(self,a,b):
#         return a + b

# opr = Operation()
# print(opr.add(5,5))               # 10

# print(opr.add('jas','il'))        # jasil






'Constructor overloading'


# class Student:

#     def __init__(self):
#         pass

#     def __init__(self, a,b):
#         return a + b 
    
# obj = Student()            # TypeError: Student.__init__() missing 2 required positional arguments: 'a' and 'b'

# # obj1 = Student(4,5)      # TypeError: __init__() should return None, not 'int'








'-----------------------------------------------------------------------------------'


"""



 
 Overriding (1 type )  

                 |   
                 |
                 |_________ Method Overriding


                        
 """



'Method overriding'

class Vehicle:
    def start(self):
        print('Vehicle starting')


class Bike(Vehicle):
    def start(self):
        super().start()                                   # Vehicle starting
        print("Bike starting with self Button")

b = Bike()
b.start()                                                 # Bike starting with self Button


