# The 'raise' statement is used to trigger an exception manually in your code.
# You can use it to raise built-in exceptions or user-defined exceptions.

# Example 1: Raising a built-in exception
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Your age is:", age)
except ValueError as e:
    print("Exception raised:", e)

# Example 2: Raising a user-defined exception
class CustomError(Exception):
    pass

def check_number(num):
    if num > 100:
        raise CustomError("Number is too large!")
    return num

try:
    check_number(150)
except CustomError as e:
    print("Custom exception raised:", e)

# Example 3: Using assert statement
# The assert statement is used to test if a condition is True. If not, it raises an AssertionError.
def get_positive_number(n):
    assert n > 0, "Number must be positive!"
    return n

try:
    get_positive_number(-10)
except AssertionError as e:
    print("AssertionError raised:", e)
