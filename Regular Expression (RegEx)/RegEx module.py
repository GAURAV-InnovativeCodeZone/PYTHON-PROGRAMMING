"""
========================== Regular Expression ==========================

A Regular Expression (RegEx) is a special string pattern used to match, search, and manipulate text using a concise syntax.
Python provides the 're module' for working with RegEx.
"""

# importing re module
import re

text = "My email is john.doe@example.com and my phone is 123-456-7890."

# Compile for reuse
pattern_email = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

# Search
m = pattern_email.search(text)
print(m.group())  # john.doe@example.com

# Find all digits
numbers = re.findall(r'\d+', text)
print(numbers)  # ['123', '456', '7890']

# Replace digits with X
masked = re.sub(r'\d', 'X', text)
print(masked)
