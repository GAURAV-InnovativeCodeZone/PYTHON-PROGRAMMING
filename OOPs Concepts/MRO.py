'''
MRO (Method Resolution Order) : The order in which Python looks for a method in a hierarchy of classes.
It is important in multiple inheritance scenarios and used to resolve the diamond problem ambiguity.
To determine which method will be called when a method is invoked on an instance of a class that inherits from multiple classes.
The MRO is determined by the C3 linearization algorithm, which ensures a consistent order of method resolution.
It can be accessed using the __mro__ attribute or the mro() method of a class.
'''

# Understanding Example of Method Resolution Order (MRO)
class A:
    pass
class B():
    pass
class C():
    pass
class D(A, B, C):
    pass
class E(B, C):
    pass
class F(D, E):
    pass

# Using the __mro__ attribute to get the method resolution order
print(F.__mro__)
# Output: (<class '__main__.F'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>)

# Using the mro() method to get the method resolution order
print(F.mro())
# Output: [<class '__main__.F'>, <class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class 'object'>]

# Demonstrating Method Resolution Order (MRO) in action

class X:
    def method(self):
        print("Method in class X")

class Y(X):
    def method(self):
        print("Method in class Y")
        super().method()

class Z(X):
    def method(self):
        print("Method in class Z")
        super().method()

class A(Y, Z):
    def method(self):
        print("Method in class A")
        super().method()

a = A()
a.method()