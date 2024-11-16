# Implementation of encapsulation with protected access specifier:
# Data encapsulation in python is implemented using protected and public access specifiers, which control the visibility of data and methods.

# Python program to demonstrate protected members

# Creating a base class
class Base:
    def __init__(self):

        self._a = 2  # Protected member

# Creating a derived class
class Derived(Base):
    def __init__(self):

        # Calling constructor of Base class
        Base.__init__(self)
        print("Calling protected member of base class: ", 
              self._a)

        # Modify the protected variable:
        self._a = 3
        print("Calling modified protected member outside class: ",
              self._a)

# driver code
obj1 = Derived()
obj2 = Base()

# Accessing the protected variable outside the class

print("Accessing protected member of obj1: ", obj1._a)
print("Accessing protected member of obj2: ", obj2._a)
