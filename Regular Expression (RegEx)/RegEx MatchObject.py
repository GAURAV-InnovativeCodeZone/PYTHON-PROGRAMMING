"""
===================== Match object =====================

When you use .match(), .search(), .finditer(), they return a Match object if a match is found.
.group()	 → Returns the matched string
.start()	 → Start index of match
.end()	     → End index of match
.span()	     → Tuple (start, end)
.groups()	 → Returns a tuple of all groups
.groupdict() → Returns named groups as dict
"""

import re

text = "abc 123 abc"
m = re.search(r"\d+", text)
print(m.group()) # 123
print(m.start()) # 4
print(m.end())   # 7
print(m.span())  # (4, 7)
print(m.groupdict())