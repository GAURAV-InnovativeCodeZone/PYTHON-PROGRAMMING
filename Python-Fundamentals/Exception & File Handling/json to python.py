'''
Example: Convert JSON to Python Object
--------------------------------------
This example demonstrates how to convert JSON data(string or file) into Python objects using the json module.
# Import the json module
# Use json.loads() to convert a JSON string to a Python object
# Use json.load() to convert JSON data from a file to a Python object
'''

import json


# Example JSON string (list of people)
json_str = '[{"name": "Gaurav", "age": 22, "city": "Delhi"}, {"name": "Amit", "age": 25, "city": "Mumbai"}]'

# Convert JSON string to Python object (list of dictionaries)
people = json.loads(json_str)
print("Python object from string (list of people):")
for idx, person in enumerate(people, 1):
    print(f"  Person {idx}: {person}")

# Read JSON data from a file and convert to Python object
try:
    with open("person.json", "r") as file:
        people_from_file = json.load(file)
    print("\nPython object from file (list of people):")
    for idx, person in enumerate(people_from_file, 1):
        print(f"  Person {idx}: {person}")
except FileNotFoundError:
    print("\nFile 'person.json' not found. Please run the 'python to json.py' script first.")

