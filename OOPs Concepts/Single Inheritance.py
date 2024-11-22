'''
★ Single Inheritance ★
This is the simplest form of inheritance where a child class inherits attributes and methods from only one parent class.
'''

# Parent class
class Parent:
    def ParentMethod(self):
        print ("calling parent method inside the parent class.")

# Child class
class Child(Parent):
    def ChildMethod(self):
        print("calling child method inside the child class.")

# instance of child class
c = Child()
c.ChildMethod()
c.ParentMethod()