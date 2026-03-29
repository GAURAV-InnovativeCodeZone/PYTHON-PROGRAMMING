'''
Demonstration of the with statement in Python for resource management
The with statement ensures that resources are properly acquired and released.
# For example, when working with files, it automatically closes the file after the block, so no need to call file.close().
'''

filename = "example.txt"

# Writing some sample content to the file for demonstration
with open(filename, 'w') as file:
    file.write("This is a sample text written using the with statement.\n")
    file.write("The file will be automatically closed after this block.\n")

# Reading the content of the file using with statement
with open(filename, 'r') as file:
    content = file.read()
    print("File content read using with statement:")
    print(content)
