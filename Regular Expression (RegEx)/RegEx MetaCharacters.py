"""
====================== MetaCharacters Or Special Characters ======================

.	  → Any char except newline
^	  → Start of string
$	  → End of string
[]	  → Character class
|     → OR (alternation)
()	  → Group
\	  → Escape
*	  → 0 or more
+	  → 1 or more
?	  → 0 or 1
{m}	  → Exactly m times
{m,n} → Between m and n times
"""

import re

text = """
Hello World!
This is a test file with:
- Numbers: 12345
- Emails: abc@example.com | xyz@mail.co
- Dates: 2024-07-25, 2025/12/31
- Words: apple, application, applied
- Other: test123, testABC, test
"""

# 1. . (dot) — any character except newline
any_char = re.findall(r"a.p", text)  # matches 'app', 'appl'
print("'.' Matches (a.p):", any_char)

# 2. ^ (caret) — start of string/line (with re.M)
lines_starting_with_This = re.findall(r"^This", text, re.M)
print("'^' Matches (lines starting with 'This'):", lines_starting_with_This)

# 3. $ (dollar) — end of string/line (with re.M)
lines_ending_with_excl = re.findall(r"!$", text, re.M)
print("'$' Matches (lines ending with '!'):", lines_ending_with_excl)

# 4. * — 0 or more
zero_or_more_digits = re.findall(r"test\d*", text)
print("'*' Matches (test\\d*):", zero_or_more_digits)  # test, test123

# 5. + — 1 or more
one_or_more_digits = re.findall(r"test\d+", text)
print("'+' Matches (test\\d+):", one_or_more_digits)  # test123

# 6. ? — 0 or 1
test_optional_digits = re.findall(r"test\d?", text)
print("'?' Matches (test\\d?):", test_optional_digits)  # test, test1

# 7. {m,n} — range
five_digits = re.findall(r"\d{5}", text)
print("'{m,n}' Matches (\\d{5}):", five_digits)  # 12345

# 8. [] — character set
vowels = re.findall(r"[aeiou]", text)
print("'[]' Matches (vowels):", vowels)

# 9. | — OR
apple_or_date = re.findall(r"apple|2024", text)
print("'|' Matches (apple or 2024):", apple_or_date)

# 10. () — grouping
date_parts = re.findall(r"(\d{4})[-/](\d{2})[-/](\d{2})", text)
print("'()' Matches (grouped dates):", date_parts)

# 11. \ — escape dot
emails = re.findall(r"\w+@\w+\.\w+", text)
print("'\\' Escape (emails):", emails)
