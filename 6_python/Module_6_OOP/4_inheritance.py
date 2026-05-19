
'Inheritance'

'1. Single inheritance'

# class Animal:

#     def eat(self):
#         print("Eating..")

#     def sleep(slef):
#         print('Sleeping..')


# class Dog(Animal):
#     pass

# arjun = Dog()

# arjun.eat()
# arjun.sleep()











'2. Mulilevel Inheritance'

# class Animal:

#     def eat(self):
#         print("Eating..")

#     def sleep(slef):
#         print('Sleeping..')


# class Dog(Animal):
#     def run(self):
#         print('running..')

# arjun = Dog()

# arjun.eat()
# arjun.sleep()
# arjun.run()



class Person:
    def __init__(self,name,age):
        print("Calling Parent constructor\n")
        self.name = name
        self.age = age

    def get_details(self):
        print(f'Name : {self.name}\nAge : {self.age}')
    
class Student(Person):
    def __init__(self, student_id, course ):
        print('Calling child Constructor')
        super().__init__()

        # self.s_id = student_id
        # self.course = course

jasil = Student('jasil',21)


jasil.get_details()











'3. Multiple inheritance'
