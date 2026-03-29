'''
__call__() : This method allows an instance of a class to be called as if it were a function.
It is defined by implementing the `__call__` method in a class. When an instance of the class is called, Python invokes this method.
It can take any number of arguments and can return any value, just like a regular function.

callable() : An object is considered callable if it can be called like a function.
This includes functions, methods, and instances of classes that implement the `__call__` method.
It can be checked using the built-in `callable()` function, which returns `True` if the object appears callable(object can be called), and `False` otherwise.
'''

# Example of using __call__ and callable

print("Using __call__ and callable\n")
class MyCallable:
    def __call__(self, x):
        return x ** 2

obj = MyCallable()

print("class is callable-", callable(MyCallable))        # True Every class is callable
print("object is callable-", callable(obj))              # True because obj is an instance of a class with __call__ method
print("__call__ is callable-", callable(obj.__call__))   # True because __call__ method is callable
print(obj(5))                                           # 25 # obj is called like a function, invoking the __call__ method


# Example of using without using __call__ and callable

print("\nWithout using __call__ and callable\n")
class MyClass:
    def MyMethod(self, x):
        return x * 2

obj = MyClass()

print("class is callable-", callable(MyClass))          # True Every class is callable
print("object is callable-", callable(obj))              # False because obj is an instance of a class without __call__ method
print("MyMethod is callable-", callable(obj.MyMethod))   # True  because MyMethod is a function
print(obj.MyMethod(5))                                   # 10 # MyMethod is called like a function

# Another example to check callable objects

print(callable(str))                       # True # str is a class and is callable
print(callable(str(10)))                   # True # str(10) is an instance and is callable
print(callable(len))                       # True # len is a built-in function and is callable
print(callable(len("Hello")))              # True # len("Hello") returns an integer, which is not callable
print(callable(int))                       # False # int is a class and is callable
print(callable(int(10)))                   # False # int(10) returns an integer, which is not callable
print(callable(float))                     # True # float is a class and is callable
print(callable(float(10.5)))               # False # float(10.5) returns a float, which is not callable
print(callable(bool))                      # True # bool is a class and is callable
print(callable(bool(1)))                   # False # bool(1) returns a boolean, which is not callable
print(callable(list))                      # True # list is a class and is callable
print(callable(list()))                    # False # list() returns a list, which is not callable
print(callable(range))                     # True # range is a class and is callable
print(callable(dict))                      # True # dict is a class and is callable
print(callable(dict()))                    # False # dict() returns a dictionary, which is not callable
print(callable(set))                       # True # set is a class and is callable
print(callable(set()))                     # False # set() returns a set, which is not callable
print(callable(classmethod))               # True # classmethod is a built-in function and is callable
print(callable(staticmethod))              # True # staticmethod is a built-in function and is callable
print(callable(object))                    # True # object is a class and is callable
print(callable(object()))                  # False # object() returns an instance of the base object class
print(callable(type))                      # True # type is a class and is callable
print(callable(type("Hello")))             # False # type("Hello") returns a string, which is not callable
