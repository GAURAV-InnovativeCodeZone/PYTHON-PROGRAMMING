'''
File Handling : File handling refers to the process of creating, reading, writing, and closing files using Python.
It allows you to store data permanently and retrieve it when needed.
# Basic File Handling Operations:
open(): Opens a file.
read(): Reads data from a file.
write(): Writes data to a file.
close(): Closes the file.
'''

# Example of basic file handling in Python:

# Open a file in write mode and write some text
file = open('example.txt', 'w')
file.write('Hello, Iam Gaurav.\n')
file.write('This is a file handling example.\n')
file.close()

# Open the file in read mode and read the content
file = open('example.txt', 'r')
content = file.read()
print('File content:')
print(content)
file.close()
