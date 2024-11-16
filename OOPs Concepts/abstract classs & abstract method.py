""" 
Abstract Class : It is a class that has one or more abstract methods, which are methods declared but not defined within the class. An abstract class cannot be instantiated on its own.
Abstract Method : It is a method that has declaration but no implementation. We have to use '@abstractmethod' decorator to define abstract method.
"""

from abc import ABC, abstractmethod


# This class is inheriting from the ABC (Abstract Base Class) module.
class car(ABC):
    def wheel(self):
        print("\nEvery car has 4 wheels.")

    # The `@abstractmethod` decorator is used to define an abstract method
    @abstractmethod
    def speed(self):
        pass

class audi(car):
    def speed(self):
        print("Audi's speed is 250 km/hr")

class maruti(car):
    def speed(self):
        print("Maruti's speed is 200 km/hr")

a = audi()
a.wheel()
a.speed()

m = maruti()
m.wheel()
m.speed()
