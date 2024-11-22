''' 
★ Hybrid Inheritance ★
Hybrid inheritance in Python is a combination of multiple and hierarchical inheritance.
In this scenario, two or more classes are derived from a single base class using hierarchical inheritance, and then a new class is derived from these subclasses using multiple inheritance.
'''

# Base class
class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, my name is {self.name}")

# Subclass 1
class Teacher(Person):
    def teach(self, subject):
        print(f"{self.name} is teaching {subject}")

# Subclass 2
class Student(Person):
    def study(self, subject):
        print(f"{self.name} is studying {subject}")

# Subclass 3
class SeniorTeacher(Teacher):
    def mentor(self, student):
        print(f"{self.name} is mentoring {student.name}")

# Subclass 4
class GiftedStudent(Student):
    def research(self, topic):
        print(f"{self.name} is researching {topic}")

# Subclass 5
class AthleticStudent(Student):
    def practice(self, sport):
        print(f"{self.name} is practicing {sport}")

# Subclass 6
class Principal(SeniorTeacher):
    def address_assembly(self):
        print(f"{self.name} is addressing the assembly")

# Creating instances
teacher = Teacher("Mr. Smith")
student1 = Student("Alice")
student2 = GiftedStudent("Bob")
athletic_student = AthleticStudent("Charlie")
senior_teacher = SeniorTeacher("Dr. Johnson")
principal = Principal("Mrs. Thompson")

# Demonstrating functionality
teacher.introduce()
teacher.teach("Mathematics")

student1.introduce()
student1.study("Science")

student2.introduce()
student2.research("Quantum Physics")

athletic_student.introduce()
athletic_student.practice("Basketball")

senior_teacher.introduce()
senior_teacher.mentor(student1)

principal.introduce()
principal.address_assembly()