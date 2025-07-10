'''
super() function :
It is used to call methods from a parent class.
It allows you to access inherited methods that have been overridden in a child class.
It enables you to extend or modify the behavior of inherited methods.
This is particularly useful for initializing parent class attributes or calling parent class methods.
This function returns a temporary object of the superclass that allows you to call its methods.
'''

class Computer:
    def __init__(self):
        self.ram = "8gb"
        self.storage ="512gb"
        print("Computer class constructor called")

class Laptop(Computer):
    def __init__(self):
        super().__init__()  # Call the constructor of the Computer class
        self.battery = "5000mah"
        print("Laptop class constructor called")
        
# Create an instance of Laptop
my_laptop = Laptop()
print(my_laptop.__dict__)    # To check content of all method inside the class in form of dictionary

print('From parent class')
print(f'Ram- {my_laptop.ram} and Storage- {my_laptop.storage}')
print('From child class')
print(f'Battery- {my_laptop.battery}'
      )