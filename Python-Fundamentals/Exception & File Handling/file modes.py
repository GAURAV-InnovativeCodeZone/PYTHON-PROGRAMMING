# Demonstration of file modes in Python

# Common file modes:
# 'r'  : Read (default) - Opens a file for reading, error if file does not exist
# 'w'  : Write - Opens a file for writing, creates file if not exists, truncates if exists
# 'a'  : Append - Opens a file for appending, creates file if not exists
# 'r+' : Read and Write - Opens a file for both reading and writing, error if file does not exist
# 'w+' : Write and Read - Opens a file for both writing and reading, creates file if not exists, truncates if exists
# 'a+' : Append and Read - Opens a file for both appending and reading, creates file if not exists
# 'b'  : Binary mode - Can be added to other modes for binary files (e.g., 'rb', 'wb')

filename = "file_mode.txt"

# Write mode ('w') example - creates or truncates the file
with open(filename, 'w') as file:
    file.write("This is written in write mode.\n")

# Append mode ('a') example - appends to the file
with open(filename, 'a') as file:
    file.write("This line is appended.\n")

# Read mode ('r') example - reads the file content
with open(filename, 'r') as file:
    content = file.read()
    print("Content read in 'r' mode:")
    print(content)

# Read and write mode ('r+') example
with open(filename, 'r+') as file:
    content = file.read()
    print("Content read in 'r+' mode before writing:")
    print(content)
    file.write("Adding a line in r+ mode.\n")

# Write and read mode ('w+') example - truncates file
with open(filename, 'w+') as file:
    file.write("This is written in w+ mode.\n")
    file.seek(0)
    content = file.read()
    print("Content read in 'w+' mode after writing:")
    print(content)

# Append and read mode ('a+') example
with open(filename, 'a+') as file:
    file.write("This line is appended in a+ mode.\n")
    file.seek(0)
    content = file.read()
    print("Content read in 'a+' mode after appending:")
    print(content)
