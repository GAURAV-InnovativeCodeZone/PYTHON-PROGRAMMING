"""
File Handling in binary mode : 
Binary mode is used for non-text files like images, audio, executable files, or any other file that contains data in binary format.

In Python, binary files are handled by opening the file in binary mode. This is done by adding 'b' to the mode string when opening a file.
such as 'rb' for reading binary files or 'wb' for writing binary files.
"""
# Example: Writing and reading a binary file

# Writing binary data to a file
with open('example.bin', 'wb') as binary_file:
    binary_file.write(b'This is binary data')

# Reading binary data from a file
with open('example.bin', 'rb') as binary_file:
    data = binary_file.read()
    print(data)  # Output: b'This is binary data'
