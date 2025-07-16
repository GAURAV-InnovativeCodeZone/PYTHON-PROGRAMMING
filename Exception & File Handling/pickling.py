"""
Pickling (Serialization):
This is a process of converting an python object into a byte stream.
This byte stream can be stored in a file or sent over a network
"""
# pickling.py
# This file demonstrates how to pickle (serialize) Student objects and save them to a file in Python.

import pickle, studentPKL as stu
    
n = int(input('Enter Number of Students : '))
with open('pickled_data.pkl', 'wb') as f:
    for i in range(n):
        name = input("Enter Student Name : ")
        roll = int(input("Enter Roll Number : "))
        address = input("Enter Address : ")
        s = stu.Student(name, roll, address)
        pickle.dump(s, f)
print('Pickling Done !!...Your data added to the file')
