"""
====================== Core Methods in re Module ======================

re.match()	    → Matches a pattern only at the beginning of the string
re.fullmatch()	→ Matches the entire string
re.search()	    → Searches for first occurrence
re.findall()	→ Finds all matches, returns list
re.finditer()	→ Finds all matches, returns iterator of Match objects
re.split()	    → Splits string by pattern
re.sub()	    → Substitutes pattern with replacement
re.subn()	    → Same as sub(), but returns tuple (new_string, number_of_subs)
re.compile()	→ Compiles a RegEx into a Pattern object for reuse
"""

import re

text = "abc 123 abc"

# match()
print(re.match(r"abc", text))   # Match at start

# search()
print(re.search(r"123", text))  # Match anywhere

# findall()
print(re.findall(r"abc", text)) # ['abc', 'abc']

# finditer()
for m in re.finditer(r"abc", text):
    print(m.start(), m.group()) # 0 abc, 8 abc

# sub()
print(re.sub(r"abc", "xyz", text)) # xyz 123 xyz

# subn()
print(re.subn(r"abc", "xyz", text)) # ('xyz 123 xyz', 2)

# split()
print(re.split(r"\s", text)) # ['abc', '123', 'abc']

# compile()
pattern = re.compile(r"abc")
print(pattern.findall(text)) # ['abc', 'abc']
