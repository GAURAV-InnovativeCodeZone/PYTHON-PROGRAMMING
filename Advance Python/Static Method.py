'''
Static Method : These method doesn't use the self parameter.
A static method does not receive an implicit first argument (don't use self parameter).
Convert a function to be a static method. To declare a static method, we use @staticmethod that is decorator.
It work at class level but not related to the class or object and it can be called either on the class (e.g. C.f()) or on an instance.
'''

class Student:
    @staticmethod
    def greeting(name):
        return f"Hello! {name}"
print(Student.greeting("Gaurav"))

class MathUtils:
    
    @staticmethod
    def square(number):
        return number * number
    
    @staticmethod
    def factorial(num):
        if num == 0:
            return 1
        else:
            return num * MathUtils.factorial(num-1)

# Calling static methods
print(MathUtils.square(5))
print(MathUtils.factorial(4))