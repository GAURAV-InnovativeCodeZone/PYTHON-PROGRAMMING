'''
Circle Class with Property Decorators Example
This example demonstrates the use of @property, @setter, and computed properties in Python classes.
'''

class Circle:
    def __init__(self, radius):
        self._radius = radius    # instance variable

    @property                # getter method
    def radius(self):
        return self._radius

    @radius.setter           # setter method
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        return 3.14 * (self._radius ** 2)

c = Circle(5)
print(c.radius)      # radius as attribute

print(c.area)        # area as attribute

c.radius = 10        # update radius using setter
print(c.area)        # area will be automatically updated