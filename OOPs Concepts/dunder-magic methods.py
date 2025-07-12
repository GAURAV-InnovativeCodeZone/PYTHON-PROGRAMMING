'''
Dunder/Magic Methods : It is a special methods in python that start and end with double underscores.
They are also known as magic methods.
They allow you to define the behavior of your objects for built-in operations.
# Common dunder methods include:
# __init__(),__str__(),__add__(),__len__(),__getitem__(),__setitem__(),__delitem__(),
# __iter__(),__next__(),__call__(),__eq__(),__enter__() and __exit__(), etc.
They can be used to implement operator overloading, type conversion, and other functionalities.
'''

# This class demonstrates the use of various dunder methods.

class Magic_Class:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Magic_Class with value: {self.value}"

    def __add__(self, other):
        if isinstance(other, Magic_Class):
            return Magic_Class(self.value + other.value)
        return NotImplemented

    def __len__(self):
        return len(str(self.value))

    def __getitem__(self, key):
        return str(self.value)[key]

    def __setitem__(self, key, value):
        temp = list(str(self.value))
        temp[key] = value
        self.value = ''.join(temp)

    def __delitem__(self, key):
        temp = list(str(self.value))
        del temp[key]
        self.value = ''.join(temp)

    def __iter__(self):
        return iter(str(self.value))

    def __next__(self):
        return next(iter(str(self.value)))

    def __call__(self):
        return f"Called MyClass with value: {self.value}"
    
    def __eq__(self, other):
        if isinstance(other, Magic_Class):
            return self.value == other.value
        return NotImplemented
    def __lt__(self, other):
        if isinstance(other, Magic_Class):
            return self.value < other.value
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Magic_Class):
            return self.value > other.value
        return NotImplemented
    def __le__(self, other):
        if isinstance(other, Magic_Class):
            return self.value <= other.value
        return NotImplemented
    def __ge__(self, other):
        if isinstance(other, Magic_Class):
            return self.value >= other.value
        return NotImplemented
    def __ne__(self, other):
        if isinstance(other, Magic_Class):
            return self.value != other.value
        return NotImplemented
    def __contains__(self, item):
        return str(item) in str(self.value)
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        return False
# Example usage
if __name__ == "__main__":
    obj1 = Magic_Class(10)
    obj2 = Magic_Class(20)
    print(obj1)  # Magic_Class with value: 10
    print(obj2)  # Magic_Class with value: 20
    obj3 = obj1 + obj2
    print(obj3)  # Magic_Class with value: 30  
    print(len(obj1))  # 2

    