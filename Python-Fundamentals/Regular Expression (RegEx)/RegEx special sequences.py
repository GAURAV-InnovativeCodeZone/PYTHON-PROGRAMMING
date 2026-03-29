"""
===================== Special Sequences =====================
These are escape codes that simplify common patterns:
\A  → Matches if the string begins with the given character
\b	→ Matches empty string at word boundary
\B	→ Matches empty string NOT at word boundary
\d	→ Matches any digit (0-9)
\D	→ Matches any non-digit
\s	→ Matches any whitespace
\S	→ Matches any non-whitespace
\w	→ Matches any alphanumeric char + _
\W	→ Matches any non-word char
\Z  → Matches if the string ends with the given regex
"""

import re

text = """
Hello123, this is a test_text!
Emails: user@example.com, test123@mail.co
Tabs\tand newlines\nare here.
"""

# 1. \d — digits
digits = re.findall(r"\d", text)
print("Digits (\\d):", digits)

# 2. \D — non-digits
nondigits = re.findall(r"\D", text)
print("Non-digits (\\D):", nondigits[:20], "...")  # show first 20 for brevity

# 3. \w — word characters
word_chars = re.findall(r"\w", text)
print("Word characters (\\w):", word_chars)

# 4. \W — non-word characters
nonword_chars = re.findall(r"\W", text)
print("Non-word characters (\\W):", repr(nonword_chars))

# 5. \s — whitespaces
whitespaces = re.findall(r"\s", text)
print("Whitespace characters (\\s):", repr(whitespaces))

# 6. \S — non-whitespaces
nonwhitespaces = re.findall(r"\S", text)
print("Non-whitespace characters (\\S):", nonwhitespaces[:20], "...")

# 7. \b — word boundaries: words only
words = re.findall(r"\b\w+\b", text)
print("Words (\\b):", words)

# 8. \B — not at a word boundary: double letters inside words
double_letters = re.findall(r"\B\w\B", text)
print("Not word boundary (\\B):", double_letters)

# 9. \A — match only if at start of string
starts_with_hello = re.match(r"\AHello", text)
print("Starts with 'Hello' (\\A):", bool(starts_with_hello))

# 10. \Z — match only if at end of string
ends_with_here = re.search(r"here\.\Z", text)
print("Ends with 'here.' (\\Z):", bool(ends_with_here))

