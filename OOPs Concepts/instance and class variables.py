'''
instance variable : A variable that is bound to the instance of the class.
class variable : A variable that is bound to the class itself.
'''

class Employee:
    increament = 3          # class variable: shared by all instances
    Total_Employee = 0
    
    def __init__(self, fname, lname, salary):
        self.fname = fname        # instance variable: unique to each instance
        self.lname = lname
        self.salary = salary
        self.increament = 2     # instance variable: shadows class variable for this instance
        Employee.Total_Employee += 1
        
    def increase(self):
        # salary1 uses class variable increament
        self.salary1 = int(self.salary * Employee.increament)
        # salary2 uses instance variable increament
        self.salary2 = int(self.salary * self.increament)
        
print("\nTotal number of employee : ", Employee.Total_Employee,"\n")

employee1 = Employee("Gaurav", "Panwar", 100000)
employee2 = Employee("Rohit", "Panwar", 200000)

print(f"Name : {employee1.fname} {employee1.lname}, Salary : {employee1.salary}")
print(f"Name : {employee2.fname} {employee2.lname}, Salary : {employee2.salary}")

employee1.increase()
print("Salary after increament : ", employee1.salary1)    # using class variable increament
employee2.increase()
print("Salary after increament : ", employee2.salary2)    # using instance variable increament

print("\nTotal number of employee : ", Employee.Total_Employee,"\n")