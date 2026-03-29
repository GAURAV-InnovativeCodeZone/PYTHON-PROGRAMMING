'''
Example: Convert Python object to JSON
---------------------------------------
This example demonstrates how to convert a Python object to JSON data(string or file) using the json module.
# Import the json module
# Create a Python object (e.g., dictionary)
# Use json.dumps() to convert the object to a JSON string (doesn't create file)
# Use json.dump() to write the object as JSON to a file (creates file)
'''

import json


# Decide how many entries to add
num_entries = int(input("How many people's data do you want to add? "))
people = []

for i in range(num_entries):
    print(f"\nEntry {i+1}:")
    name = input("  Enter Name: ")
    age = int(input("  Enter Age: "))
    city = input("  Enter City: ")
    person = {
        "name": name,
        "age": age,
        "city": city
    }
    people.append(person)

# Convert Python Objects to JSON string
json_str = json.dumps(people, indent=4)
print("\nJSON string:")
print(json_str)

# Write list of Python Objects to a JSON file
with open("person.json", "w") as file:
    json.dump(people, file, indent=2)
print("\nData has been written to person.json file.")

