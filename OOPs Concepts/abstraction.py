from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class square(shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side**2
    
class rectangle(shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
    
class circle(shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        from math import pi
        return pi * (self.radius ** 2)

class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height
    
# Creating an instance(object)
s = square(2)
r = rectangle(5, 7)
c = circle(3)
t = triangle(4, 6)
print("Area of square : ", s.area())
print("Area of rectangle : ", r.area())
print("Area of circle : ", c.area())
print("Area of triangle : ", t.area())
