'''
Constructor :
In Python, a constructor is a special method that is automatically called when an object of a class is created.
It is used to initialize the attributes of the class.
The constructor method is defined using the __init__() function.

Destructor :
A destructor is a special method that is called when an object is about to be destroyed.
The destructor method is defined using the __del__() function.
Destructor is used to perform cleanup operations, such as closing files or releasing resources.
'''

class Person:
    
    # Constructor
    # The __init__ method is called when an object of the class is created.
    def __init__(self, fname, lname):
        self.name = fname + " " + lname
        print(f"Constructor called for {self.name}")

    # Destructor
    # The __del__ method is called when an object is about to be destroyed.
    def __del__(self):
        print(f"Destructor called for {self.name}")
        del self.name  # Optional: Clean up the name attribute

# Creating an object of the Person class
p = Person("Gaurav", "Panwar")
print(p.name)  # Output: Gaurav Panwar
print(p.__dict__)  # Output: {'name': 'Gaurav Panwar'}

# Deleting the object
del p  # This will call the destructor
# Note: The destructor is called when the object is deleted or goes out of scope.

# Note: The destructor may not be called immediately after the object is deleted, as Python uses garbage collection.
# To ensure the destructor is called, you can use the del statement or let the object go out of scope.
