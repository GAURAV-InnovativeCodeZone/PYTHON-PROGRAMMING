"""
=================== Regex Flags ===================

re.I or re.IGNORECASE	→ Ignore case
re.M or re.MULTILINE	→ ^ & $ match at each line
re.S or re.DOTALL	    → Dot matches newline too
re.X or re.VERBOSE	    → Allow whitespace/comments in pattern
re.A or re.ASCII	    → ASCII-only matching
"""

import re

text = "Hello\nworld"

print(re.findall(r"^world", text)) # []
print(re.findall(r"^world", text, re.M)) # ['world']

print(re.findall(r".+", text)) # ['Hello', 'world']
print(re.findall(r".+", text, re.S)) # ['Hello\nworld']

print(re.findall(r"hello", text, re.I)) # ['Hello']
