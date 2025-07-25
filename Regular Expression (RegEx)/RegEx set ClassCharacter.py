"""
================== Regex Sets (Character Classes) ==================

A character class (set) lets you match any one character from a defined group:
A Set matches any one of specified characters.

[abc]        → matches a, b, or c
[a-z]        → matches any lowercase letter
[A-Z]        → matches any uppercase letter
[0-9]        → matches any digit
[^abc]       → matches any character except a, b, or c (negated set)
[A-Za-z]     → Any letter
[a-zA-Z0-9_] → matches any word character (similar to \w)
[aeiou]      → matches any vowel
"""

import re

text = """
This is a Sample Text with:
- Lowercase: abcxyz
- Uppercase: ABCXYZ
- Digits: 123456
- Special chars: !@#$%^&*
- Mixed: A1b2C3xYz!
"""

# 1. Find all lowercase letters [a-z]
lowercase = re.findall(r"[a-z]", text)
print("Lowercase letters:", lowercase)

# 2. Find all uppercase letters [A-Z]
uppercase = re.findall(r"[A-Z]", text)
print("Uppercase letters:", uppercase)

# 3. Find all digits [0-9]
digits = re.findall(r"[0-9]", text)
print("Digits:", digits)

# 4. Find all vowels [aeiouAEIOU]
vowels = re.findall(r"[aeiouAEIOU]", text)
print("Vowels:", vowels)

# 5. Find all characters except letters and digits [^a-zA-Z0-9]
specials = re.findall(r"[^a-zA-Z0-9\s]", text)  # \s to ignore whitespace
print("Special characters:", specials)

# 6. Find any letter followed by a digit [a-zA-Z][0-9]
letter_digit = re.findall(r"[a-zA-Z][0-9]", text)
print("Letter followed by digit:", letter_digit)

# 7. Find any sequence of 3 characters: [A-Z][0-9][a-z]
pattern = r"[A-Z][0-9][a-z]"
matches = re.findall(pattern, text)
print("Pattern [A-Z][0-9][a-z]:", matches)
