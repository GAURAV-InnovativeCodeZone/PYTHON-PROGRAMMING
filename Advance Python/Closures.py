'''
Closures :
A closure is a function that retains the bindings of its lexical scope, even when the function is executed outside that scope.
In Python, closures are created when a nested function references variables from its enclosing scope.
'''

def outer_function(msg):
    def inner_function():
        print(msg)
    return inner_function

closure = outer_function("Hello, World!")
closure()  # Output: Hello, World!
