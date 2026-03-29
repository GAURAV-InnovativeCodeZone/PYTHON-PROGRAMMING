'''
Class Variable : 
Class variables are variables that are shared among all instances of a class.
They are defined within the class but outside any instance methods.

Class Method :
Class methods are methods that operate on class variables. 
They are defined using the @classmethod decorator and take the class as the first argument (usually named cls).
'''

class Student:
    school_name = "ABC School"  # class variable

    def __init__(self, location):
        self.location_name = location  # instance variable

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name  # class method to change class variable

# create instances
s1 = Student("Tehri Garhwal")
s2 = Student("Dehradun")

# accessing instance variable
print("Location:", s1.location_name)  # Tehri Garhwal

# accessing class variable via class
print("Old school name:", Student.school_name)  # ABC School

# changing class variable using class method via instance (also works via class)
s1.change_school_name("XYZ School")

# accessing class variable after change via class
print("New school name:", Student.school_name)  # XYZ School

# accessing class variable via instance
print("School name from s2:", s2.school_name)  # XYZ School
