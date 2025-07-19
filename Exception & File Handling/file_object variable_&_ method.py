'''
File Object Variables (Attributes):
  - name: The name of the file.
  - mode: The mode in which the file was opened (e.g., 'r' for read, 'w' for write, 'a' for append).
  - closed: A boolean indicating whether the file is closed (True) or open (False).

File Object Methods:
  - write(): Writes a string to the file.
  - writelines(): Writes a list of strings to the file.
  - read(): Reads the entire content of the file.
  - readline(): Reads a single line from the file.
  - readlines(): Reads all lines of the file into a list.
  - close(): Closes the file.
  - readable(): Returns True if the file was opened in a mode that allows reading.
  - writable(): Returns True if the file was opened in a mode that allows writing.
'''
# Demonstration of file object variables(attributes) and methods in Python

filename = "file_attribute.txt"

# Open the file in write mode and write some lines
with open(filename, 'w') as file:
    print(f"File name: {file.name}")
    print(f"File mode: {file.mode}")
    file.write("Line 1: This is the first line.\n")
    file.write("Line 2: This is the second line.\n")
    file.write("Line 3: This is the third line.\n")

# Demonstrate writelines() method to write multiple lines at once
lines_to_write = ["Line 4: This is the fourth line.\n", "Line 5: This is the fifth line.\n"]
with open(filename, 'a') as file:
    file.writelines(lines_to_write)

# Open the file in read mode and demonstrate different read methods
with open(filename, 'r') as file:
    print(f"\nReading entire content using read():")
    content = file.read()
    print(content)

with open(filename, 'r') as file:
    print(f"\nReading line by line using readline():")
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()

with open(filename, 'r') as file:
    print(f"\nReading all lines into a list using readlines():")
    lines = file.readlines()
    for line in lines:
        print(line, end='')

# Demonstrate file object attributes
file = open(filename, 'r')
print(f"\nFile name attribute: {file.name}")
print(f"File mode attribute: {file.mode}")
print(f"Is file closed? {file.closed}")
file.close()
print(f"Is file closed after close()? {file.closed}")

# Demonstrate readable() and writable() methods
file = open(filename, 'r')
print(f"\nIs the file readable? {file.readable()}")
print(f"Is the file writable? {file.writable()}")
file.close()

file = open(filename, 'a')
print(f"\nIs the file readable? {file.readable()}")
print(f"Is the file writable? {file.writable()}")
file.close()
