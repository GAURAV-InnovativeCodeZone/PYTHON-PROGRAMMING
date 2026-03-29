'''
JSON (JavaScript Object Notation):
JSON is a lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate.
It is commonly used for transmitting data in web applications between a server and a client.

Common functions in Python's json module:
1. json.dump(obj, file)         # Serialize obj as a JSON formatted stream to file (creates file)
2. json.dumps(obj)              # Serialize obj to a JSON formatted string (doesn't create file)
3. json.load(file)              # Deserialize JSON from a file to a Python object
4. json.loads(s)                # Deserialize JSON from a string to a Python object
'''

# Example usage of json module functions
import json

# Example Python object (dictionary)
data = {"name": "Alice", "age": 25, "city": "New York"}

# 1. Serialize obj as a JSON formatted stream to file
with open("data.json", "w") as f:
    json.dump(data, f)

# 2. Serialize obj to a JSON formatted string
json_str = json.dumps(data)
print("Serialized to string:", json_str)

# 3. Deserialize JSON from a file to a Python object
with open("data.json", "r") as f:
    data_from_file = json.load(f)
print("Deserialized from file:", data_from_file)

# 4. Deserialize JSON from a string to a Python object
data_from_str = json.loads(json_str)
print("Deserialized from string:", data_from_str)

