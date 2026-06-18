
'Abstract'

# from abc import ABC, abstractmethod

'''

abc                -> Module
ABC                -> Class
abstractmethod     -> decerator


'''







'..................................................................................'







from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def breaks(self):
        pass

    def acceleration(self):
        print("Vehicle is accelerating")


class Bike(Vehicle):

    def breaks(self):
        print("Bike brakes applied")


b = Bike()

b.breaks()
b.acceleration()