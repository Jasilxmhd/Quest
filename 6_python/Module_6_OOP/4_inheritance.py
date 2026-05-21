
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







# class Person:
#     def __init__(self,name,age):
#         print("Calling Parent constructor\n")
#         self.name = name
#         self.age = age


    
# class Devolper(Person):
#     def __init__(self, name , age, salary , language ):
#         super().__init__(name,age)
#         self.salary = salary
#         self.language = language

#     def get_details(self):
#         print(f'Name : {self.name}\nAge : {self.age}\nSalary : {self.salary}\nLanguage : {self.language}')

# jasil = Devolper(name='Jasil', salary=45000, age=21, language="Python")


# jasil.get_details()








'multilevel inheritance'

# class Vehicle:                                      #class 1 grand parent
    
#     def start(self):
#         print("Vehicle can start..")
        
#     def test(self):
#         print("Testing Vehicle method....")

# class Car(Vehicle):                                 #class 2 parent
#     def horn(self):
#         print("Horn......")
#     def test(self):
#         super().test()
#         print("Testing Car method....")
        
# class Ev(Car):                                      #class 3 child
#     def test(self):
#         super().test()
#         print("Testing Ev method....")


# nexon=Ev()

# nexon.horn()
# nexon.start()

# bmw=Vehicle()
# bmw.start()

# nexa=Ev()
# nexa.test()






'Multiple inheritance'

# class Sport:                                                # Parent 1
#     team = 'India'

#     def action(self):
#         print('Playing football')


# class Musician:                                            # Parent 2
#     band = 'thaikudam'
#     def ma(self):
#         print("playing gitar")


# class student(Sport,Musician):
#     def study(self):
#         print('Studies in college')


# jasil = student()                                            # child

# print(jasil.team)           # child class il kodukkunna reethiyil print aavum
# print(jasil.band)

# jasil.action()

# print(student.mro())










'Hierarchical inheritance'

# class Shape:                                                  # Parent
#     def color(self):
#         print("Green")

# class Circle(Shape):                                          # child 1
#     def area(self,r):
#         print('Cirle Area :', 3.14*r**2)

# class Rectangle(Shape):                                      # child 2
#     def area(self,l,b): 
#         print('Rectangle area :',l * b)

# c1 = Circle()
# c1.area(3)
# c1.color()


# r1 = Rectangle()
# r1.area(5,5)
# r1.color()









'Hybrid inheritance'

# class Vehicle:
#     def fuel_type(self):
#         print('Vehicles use same fuel type.')


# class Car(Vehicle):
#     def wheels(self):
#         print('Car has 4 wheels.')


# class Motorcycle(Vehicle):
#     def wheels(self):
#         print('Motorcycle has 2 wheels.')


# class ElectricCar(Car):
#     def battery(self):
#         print('Electric Car use litium battery.')


# class ElectricMotorcycle(Motorcycle):
#     def battery(self):
#         print('Electric Motor cycle Car use litium battery.')

# ec = ElectricCar()
# ec.battery()
# ec.fuel_type()
# ec.wheels()


# c = Car()
# c.fuel_type()
# c.wheels()



# motor = Motorcycle()
# motor.fuel_type()
# motor.wheels()


# em = ElectricMotorcycle()
# em.battery()
# em.fuel_type()
# em.wheels()





'Food Delivery app'

# class User:

#     def login(self):
#         print('Login sucessful')

#     def order(self):
#         print('check food items')
    
#     def payment(self):
#         print('payment ok')

# class Shop:

#     def accept_order(self):
#         print('Order Accepted ✅')


#     def food_items(self):
#         print(f'what you want  ? \n 1.ichen biriyani \n 2.Beef Biriyani \n 3.Mandi')

# class Devilery_patner:

#     def location(self):
#         print('Available to deliver ✅')


    

# class App(User,Shop,Devilery_patner):
#     def app_working(self):
#         print('✅')


# us = App()

# us.login()
# us.order()
# us.payment()

# us.accept_order()
# us.food_items()

# us.location()







