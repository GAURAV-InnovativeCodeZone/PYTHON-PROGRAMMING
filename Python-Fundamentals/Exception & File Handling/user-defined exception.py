'''
User-defined Exception:
It is a custom error type created by defining a new class that inherits from the built-in Exception class.
This allows you to raise and handle specific errors in your code.
'''

class NegativeNumberError(Exception):
    pass

def check_number(num):
    if num < 0:
        raise NegativeNumberError("Negative number not allowed.")
    return num

try:
    print(check_number(eval(input())))
except NegativeNumberError as e:
    print("Custom Exception Caught:", e)
