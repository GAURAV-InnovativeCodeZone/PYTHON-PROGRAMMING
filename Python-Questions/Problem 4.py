'''
Define a Employee classs with attributes likke role, department and salary.
Implement a Show_details method to display the employee details.
'''

class Employee:
    def __init__(self, role, department, salary):
        self.role = role 
        self.department = department 
        self.salary = salary
        
    def Show_detailes(self):
        print(f'Role: {self.role}')
        print (f'department: {self.department}')
        print(f'Salary: {self.salary}')
        
class Engineer(Employee):
    def __init__(self, name, age,):
        self.name = name
        self.age = age
        super().__init__('Engineer', 'IT Sector', 250000)

# Example usage
# Create an instance of Employee
e1 = Employee('Python Developer', 'IT', 250000)
e1.Show_detailes()

# Create an instance of Engineer()
e2 = Engineer("Gaurav", 22)
print(f'Name: {e2.name}')
print(f'Age: {e2.age}')
e2.Show_detailes()