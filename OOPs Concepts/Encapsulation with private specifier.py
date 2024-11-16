# Implementation of encapsulation with private access specifier:
# Data encapsulation in python is implemented using private and public access specifiers, which control the visibility of data and methods.

# Python program to demonstrate protected members

# Creating a Base class
class Base:
    def __init__(self):
        self.a = "Gaurav Panwar"    # public member
        self.__c = "Gaurav Singh"   # private member

# Creating a derived class
class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        # Accessing the private member using its mangled name
        print(self._Base__c)  # Accessing the private variable

# Driver code
if __name__ == "__main__":
    obj1 = Base()
    print(obj1.a)
    obj2 = Derived()

# Uncommenting print(obj1.c) will
# raise an AttributeError
# private member of base class
# is called inside derived class
