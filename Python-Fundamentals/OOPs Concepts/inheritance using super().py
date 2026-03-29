'''
Inheritance using super():
In Python, inheritance allows a class (child class) to inherit attributes and methods from another class (parent class).
The super() function is used to call methods from the parent class, enabling you to extend or modify the behavior of inherited methods.
'''

class Shape:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        print("Calculating area of the shape...")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)
        
    def area(self):
        super().area()
        print(f'Area of Rectangle: {self.length * self.width}')

class Cube(Shape):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
        
    def area(self):
        super().area()
        print(f'Area of Cube: {self.length * self.width * self.height}')

r = Rectangle(10, 5)
r.area() 
c = Cube(10, 5, 15)
c.area()
