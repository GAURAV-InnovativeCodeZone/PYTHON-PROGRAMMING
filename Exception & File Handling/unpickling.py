"""
Unpickling (Deserialization):
This is the process of converting a byte stream back into a Python object.
"""
# unpickling.py
# This file demonstrates how to unpickle and display objects from a pickle file in Python.

import pickle
import studentPKL as stu

with open('pickled_data.pkl', 'rb') as f:
    print('Unpickling Done!... Now you can see the data from the file.')  
    while True:
        try:
            obj = pickle.load(f)
            obj.display()
        except EOFError:
            break
