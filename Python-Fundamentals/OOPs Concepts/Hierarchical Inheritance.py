'''
★ Hierarchical Inheritance ★
This type of inheritance contains multiple derived classes that are inherited from a single base class.
'''

# parent class
class Manager: 
   def managerMethod(self):
      print ("I am the Manager")

# child class
class Employee1(Manager): 
   def employee1Method(self):
      print ("I am Senior Engineer")
      
      
# second child class
class Employee2(Manager): 
   def employee2Method(self):
      print ("I am Junior Engineer")
           
# creating instances
emp1 = Employee1()  
emp2 = Employee2()
# method calls
emp1.managerMethod() 
emp1.employee1Method()
emp2.managerMethod()
emp2.employee2Method()  