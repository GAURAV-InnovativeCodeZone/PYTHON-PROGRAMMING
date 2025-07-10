'''
Constructor Overloading :
In Python, constructor overloading is not directly supported as it is in some other languages like Java or C++.
However, you can achieve similar functionality by using default arguments or variable-length arguments in the constructor.
constructor overloading allows a class to have multiple constructors with different parameters, enabling the creation of objects in various ways.
'''

class Father:
    # Constructor of Father class
    # This constructor initializes the 'vehicle' attribute
    def __init__(self):
        print("Father constructor called")
        self.vehicle = 'scooter'

# Inheriting from Father class
class Son(Father):
    
    # Overriding(Inheriting) the constructor of Father class
    def __init__(self):     # derived constructor's priority is more than base class constructor
        print("Son constructor called")
        self.vehicle = 'bike'
    
s = Son()
print(s.__dict__)
print(s.vehicle)  # Output: bike