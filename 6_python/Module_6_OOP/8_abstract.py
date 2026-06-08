
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
        pass

class Bike(Vehicle):
    def breaks(self):
        return super().breaks()