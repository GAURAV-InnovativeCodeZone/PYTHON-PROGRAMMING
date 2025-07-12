'''
Define a Circle class to create a circle with radius using the constructor.
Implement Area() and Circumference() methods to calculate the area and circumference of the circle.
'''

# Define a Circle class
class Circle:
    
    # Constructor to initialize the radius of the circle
    def __init__(self, radius):
        self.radius = radius
    
    # Method to calculate the area of the circle
    def Area(self):
        return (int(3.14 * self.radius ** 2))

    # Method to calculate the circumference of the circle
    def Circumference(self):
        return (int(2 * 3.14 * self.radius))

# Example usage
# Create an instance of Circle with radius 5
c = Circle(5)

# Access the methods to calculate area and circumference
print('Area of Circle: ', c.Area())
print('Circumference of Circle: ', c.Circumference())