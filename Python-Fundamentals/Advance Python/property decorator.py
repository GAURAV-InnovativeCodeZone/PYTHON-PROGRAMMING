'''
@property decorator is used to define getter methods inside class that allow to access methods like attributes(calling them without parentheses). It has three methods getter, setter and deleter.
'''
#Use the @property Decorator to Implement Getter, Setter and Deleter Methods in a Python Class

class Employee:
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last

    @property   
    def mail(self):
        return f'{self.firstname}{self.lastname}@gmail.com'
    
    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.firstname = first
        self.lastname = last
    
    @fullname.deleter
    def fullname(self):
        print('Deleting fullname...')
        self.firstname = None
        self.lastname = None
        
# Creating instances of Employee class
e1 = Employee('gaurav', 'panwar')
e2 = Employee('rohit', 'panwar')
e3 = Employee('nikita', 'panwar')

# accessing data using getter methods as attributes
print('Accessing data using getter methods as attributes:')
print(e1.fullname)  
print(e1.mail)
print(e2.fullname)
print(e2.mail)
print(e3.fullname)
print(e3.mail)

print('----------------------------------')

# changing or modifying data using setter and then,
# accessing data using getter methods as functions
print('Accessing data using getter methods as functions:')
e1.fullname = 'steeve jobs'
print(e1.fullname)
print(e1.mail)

e2.fullname = 'alice harper'
print(e2.fullname)
print(e2.mail)

e3.fullname = 'john doe'
print(e3.fullname)
print(e3.mail)

print('----------------------------------')

# Deleting data using deleter method
del e1.fullname
print(e3.fullname)  # This will raise an error because fullname is deleted
print(e1.mail)      # This will still work because mail is a property and not deleted
