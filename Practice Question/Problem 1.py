''' create student class that takes name & marks of subjects as arguments in constructor.
Then create a method to print the average. '''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "your average score is", sum/3)

s1 = Student("Gaurav", [90, 85, 95])
s1.get_average()
s1.name = "Rohit"
s1.get_average()