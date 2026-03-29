'''
Method Overriding :
In Python, method overriding allows a derived class to provide a specific implementation of a method that is already defined in its base class.
This is useful for customizing or extending the behavior of inherited methods.
'''
# Using super() function in method overriding:
# The super() function can be used to call methods from a parent class, enabling you to extend or modify the behavior of inherited methods.

class Add:
    def result(self, a, b):
        print('Addition:', a+b)
        
class Subtract(Add):
    def result(self, a, b):
        super().result(10, 6)       # call the method from the add class
        print('Subtraction:', a-b)

class Multiply(Subtract):
    def result(self, a, b):
        super().result(10, 6)
        print('Multiplication:', a*b)

m = Multiply()
m.result(10, 6)

# if we don't use super() function then we need to write these extra lines
#without using super() function
# m = Multiply()
# m.result(10, 6)
# m = Subtract()
# m.result(10, 6)
# m = Add()
# m.result(10, 6)
