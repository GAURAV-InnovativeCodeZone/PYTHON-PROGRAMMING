'''
Built-in Exception:
Built-in exceptions in Python are standard error types that are provided by the Python language.
These exceptions are automatically raised by Python when errors occur during program execution.
such as-dividing by zero, accessing an invalid index, or using an undefined variable.
Common exception types in Python:
    - ZeroDivisionError
    - ValueError
    - TypeError
    - IndexError
    - KeyError
    - FileNotFoundError
'''

# Example 1: ZeroDivisionError
# Occurs when you divide a number by zero.
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError caught!", e)

# Example 2: ValueError
# Occurs when a function gets an argument of the right type but an inappropriate value.
try:
    num = int("abc")
except ValueError as e:
    print("ValueError caught!", e)

# Example 3: TypeError
# Occurs when an operation is applied to an object of an inappropriate type.
try:
    s = '2' + 3
except TypeError as e:
    print("TypeError caught!", e)

# Example 4: IndexError
# Occurs when accessing an invalid index in a list or tuple.
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print("IndexError caught!", e)

# Example 5: KeyError
# Occurs when accessing a dictionary with a missing key.
try:
    my_dict = {"name": "Gaurav"}
    print(my_dict["age"])
except KeyError:
    print("KeyError caught! Key not found in dictionary!")
  
# Example 6: NameError
# Occurs when a variable name is not defined.
try:
    print(a)
except NameError as e:
    print("NameError caught!", e)
    
# Example 7: FileNotFoundError
# Occurs when trying to open a file that doesn’t exist.
try:
    with open("nonexistent_file.txt") as f:
        data = f.read()
except FileNotFoundError as e:
    print("FileNotFoundError caught!", e)
    
# Example 8: AttributeError
# Occurs when an invalid attribute is referenced.
try:
    x = 5
    x.append(3)
except AttributeError as e:
    print("AttributeError caught!", e)
    
# Exxample 9: ImportError
# Occurs when an imported module or name does not exist.
try:
    import non_existent_module
except ImportError as e:
    print("ImportError!", e)

