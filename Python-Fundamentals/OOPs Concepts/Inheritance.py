                           # ★ Python Inheritance ★ #
''' 
Inheritance: Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent Class: The class that gets inherited is called a base class or parent class.
Child Class: The class that inherits another class is called a child class.

# Types of Inheritance.....

1. Single Inheritance
2. Multiple Inheritance
3. Multilevel Inheritance
4. Hierarchical Inheritance
5. Hybrid Inheritance
'''

# Creating a Parent Class
# Create a class named Person, with firstname and lastname properties, and a printname method

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def method(self):
    print(self.firstname, self.lastname)

# Create a Child Class
# Create a class named Student, which will inherit the properties and methods from the Person class

class Student(Person):
  pass

# Create an object of the Student class

x = Person("Gaurav", "Panwar")
x.method()
x = Student("Gaurav", "Singh")
x.method()