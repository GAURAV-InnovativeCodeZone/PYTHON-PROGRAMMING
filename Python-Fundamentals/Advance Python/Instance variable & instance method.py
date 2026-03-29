'''
Instance Variable : 
Instance variables are variables that are bound to the instance of the class.
They are defined within the __init__ method and are unique to each instance of the class.

Instance Method :
Instance methods are functions defined within a class that operate on instance variables.
'''

class Student:
    def __init__(self,name,age):
        
        # instance variable
        self.name = name
        self.age = age
        
    # instance method
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# creating object (instances)     
s1 = Student("Gaurav", 20)
s2 = Student("Saurav", 21)

# accessing instance variable
print(s1.name, s1.age)
print(s2.name, s2.age)

# accessing instance variable
s1 = Student("Ayush", 22)
s1.display()
