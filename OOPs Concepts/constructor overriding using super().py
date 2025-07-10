'''
Constructor Overriding using super():
In Python, you can use the super() function to call the constructor of the parent class.
This allows you to initialize the parent class's attributes while still providing the flexibility of a derived class constructor.
The super() function allows you to call methods from a parent class, enabling you to extend or modify the behavior of inherited methods.
'''

class Father:
    def __init__(self):
        print("Father constructor called")
        self.vehicle = 'scooter'

class Son(Father):
    def __init__(self):
        super().__init__()  # Call the constructor of the Father class
        print("Son constructor called")
        self.vehicle = 'bike'

s = Son()
print(s.__dict__)
print(s.vehicle)  # Output: bike
