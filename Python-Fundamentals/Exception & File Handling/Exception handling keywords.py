'''
Exception:
An exception is an event detected during execution that interrupts the normal flow of a program.
Exceptions are usually errors that occur when the program encounters something unexpected.

Exception Handling : Exception handling is the process of responding to exceptions when they occur. 
Keywords like (1.try 2.except 3.else 4.finally) used to catch and handle errors gracefully, preventing the program from crashing.
else and finally block are optional.
'''

## Example of Exception Handling using try, except, else, finally ##

# try block : wrapping the code that might raise an exception.
try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2

# except block : handling the exception.
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    
# else block : executing if no exception occurs.
else:
    print("Division result:", result)
    
# finally block : It is always executed and executing regardless of exception occurrence.
finally:
    print("Always executed! Execution is complete.")
    
