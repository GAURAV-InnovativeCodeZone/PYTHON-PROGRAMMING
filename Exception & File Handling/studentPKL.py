# studentPKL.py
# This file defines the Student class for pickling and unpickling student data.

 
class Student:
    def __init__(self, name, roll, address):
        self.name = name
        self.roll = roll
        self.address = address
        
    def display(self):
        print(f'Name : {self.name}, Roll : {self.roll}, Address : {self.address}')
    