'''
functools module:-
functools is a built-in Python module providing higher-order functions that act on or return other functions.
| Function      | Use                                                             |
| ------------- | --------------------------------------------------------------- |
|  wraps()      | Used inside decorators to preserve original function name, docs |
|  lru_cache()  | Caching function results                                        |
|  partial()    | Create a new function with fixed arguments                      |
|  reduce()     | Perform cumulative operations                                   |
'''

'''
When we make our own decorator then the decorated function loses its identity, so
@wraps decorator helps preserve the original function's metadata when it is decorated.'''

# Example without @wraps:
def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
    return wrapper

@my_decorator
def say_hello():
    print("Hello!") 

# Check function metadata/name
print(say_hello.__name__)


# Example with @wraps:(Correct way)
from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        print("Before function")
        return func(*args, **kargs)
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
    
# Check function metadata/name
print(say_hello.__name__)