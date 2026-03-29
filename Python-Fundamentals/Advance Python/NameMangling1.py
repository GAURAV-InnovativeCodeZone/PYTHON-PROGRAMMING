# The most common use of __name__ == "__main__" is to create a block of code that only runs when the script is executed directly.
# This behavior allows you to write code that can be executed both as a standalone script and as a module imported into other scripts.
# In Python, __name__ is a special variable that holds the name of the current module.
# Here's how it works:
# ● When a Python script is run directly: The __name__ variable is set to "__main__". This indicates that the script is the main program being executed.
# ● When a Python script is imported as a module: The __name__ variable is set to the name of the module itself.


def myfunc(string):
    return(f"This is a name mangling program. {string}")

def add(a,b):
    return a+b+10

print("file is",__name__)
if __name__ == '__main__':
    print(myfunc("Done!"))
    result = add(20,30)
    print("Result",result)  # Output: 60