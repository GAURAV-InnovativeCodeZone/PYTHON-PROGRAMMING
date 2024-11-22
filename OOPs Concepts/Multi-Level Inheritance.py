"""
★ Multi-Level Inheritance ★
The inheritance is archived when a derived class inherits another derived class. 
There is no limit on the number of levels up to which, the multi-level inheritance is archived in python.
It has one parent class and multiple parent classes.
"""

# parent class
class GrandFather:
    surname = "Panwar"
    def ownHouse(self):
        print("Grandpa House")
    
# derived class 1
class Father(GrandFather):
    def ownCar(self):
        print("Father's Car")

# derived class 2
class Son(Father):
    def ownBook(self):
        print("Son's Book")
        print("Inherited grandfather's surname...", self.surname)

# instance for son class
s = Son()
s.ownBook()
s.ownCar()
s.ownHouse()

# instance for father class
f = Father()
f.ownCar()
f.ownHouse()
print(f.surname)
