'''
Built-in classes and attributes in Python are fundamental components that provide a wide range of functionalities.
Here are some of the most commonly used built-in classes and their attributes:

# built-in classes:
# getattr, setattr, delattr, hasattr, type, object, int, float, str, list, dict, set, tuple, bool, etc.

# built-in attributes:
# __dict__, __class__, __name__, __module__, __doc__
'''

# Example of using built-in classes and attributes

# 1. Using built-in classes
num = int(10)        # Using the built-in int class to create an integer object
text = str("hello")   # Using the built-in str class to create a string object
lst = list([1, 2, 3])  # Using the built-in list class to create a list object

# Using built-in functions
print(text) # hello
print(type(num))  # <class 'int'>
print(isinstance(num, int))  # True
print(isinstance(num, object))  # True
print(isinstance(num, float))  # False
print(isinstance(num, str))  # False
# Using built-in functions to manipulate the object
print(num + 5)  # 15
print(num * 2)  # 20
# Using built-in functions to check and manipulate attributes
class MyClass:
    pass

obj = MyClass()


# setattr: set an attribute
setattr(obj, 'x', 100)
print(obj.x)  # 100

# getattr: get an attribute
print(getattr(obj, 'x'))  # 100

# hasattr: check if attribute exists
print(hasattr(obj, 'x'))  # True
print(hasattr(obj, 'y'))  # False

# delattr: delete an attribute (only if it exists)
if hasattr(obj, 'x'):
    delattr(obj, 'x')
print(hasattr(obj, 'x'))  # False


# 2. Using built-in attributes
print(num.__class__)  # <class 'int'>
print(num.__doc__)  # 'int([x]) -> integer\n\nConvert a string or number to an integer, if possible.'

# __dict__ and __name__ usage examples
print(int.__name__)  # 'int' (class attribute)
print(MyClass.__name__)  # 'MyClass' (class attribute)
print(obj.__dict__)  # {} (empty, since no attributes after deletion)

# Add an attribute again to see __dict__
obj.y = 200
print(obj.__dict__)  # {'y': 200}