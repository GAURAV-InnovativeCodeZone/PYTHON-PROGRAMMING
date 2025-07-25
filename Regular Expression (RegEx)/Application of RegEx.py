'''
================ Application Of RegEx ================

🔹 Websites       → Form validation (emails, passwords)
🔹 Data Science   → Cleaning messy data
🔹 Web Scraping   → Extract links, emails
🔹 Security       → Detect malicious patterns (e.g., SQL injection)
🔹 Search engines → Pattern-based search
🔹 IDEs           → Find and replace code
🔹 Log Analysis   → Track errors, user activity
'''

import re

text = """
Contact me at john.doe@example.com or jane_doe123@mail.co.uk.
Visit https://www.example.com or http://test.org for more info.
Call us at +1-800-555-1234 or (123) 456-7890.
Dates: 2025-07-25, 25/07/2025, 07-25-2025
Bad words: This is a damn test. What the hell!
My password: P@ssw0rd123!
"""

print("===== 1. Validate & Extract Emails =====")
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, text)
print("Emails:", emails)

print("\n===== 2. Extract Phone Numbers =====")
phone_pattern = r"(\+?\d{1,3}[-\s]?)?(\(?\d{3}\)?[-\s]?)\d{3}[-\s]?\d{4}"
phones = re.findall(phone_pattern, text)
# re.findall with groups returns tuples — flatten them:
flat_phones = [''.join(match) for match in phones]
print("Phone Numbers:", flat_phones)

print("\n===== 3. Find URLs =====")
url_pattern = r"https?://[^\s]+"
urls = re.findall(url_pattern, text)
print("URLs:", urls)

print("\n===== 4. Extract Dates =====")
date_pattern = r"\b(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4})\b"
dates = re.findall(date_pattern, text)
print("Dates:", dates)

print("\n===== 5. Substitute Bad Words (Censor) =====")
bad_words = ["damn", "hell"]
censored_text = text
for word in bad_words:
    censored_text = re.sub(rf"\b{word}\b", "***", censored_text, flags=re.IGNORECASE)
print("Censored Text:\n", censored_text)

print("\n===== 6. Split Text on Multiple Delimiters =====")
csv_text = "apple, orange;banana|grape mango"
split_pattern = r"[,\s;|]+"
fruits = re.split(split_pattern, csv_text)
fruits = [f for f in fruits if f]  # remove empty strings
print("Fruits:", fruits)

print("\n===== 7. Validate Password Strength =====")
password = "P@ssw0rd123!"
# At least 8 chars, 1 uppercase, 1 lowercase, 1 digit, 1 special char
password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
is_valid = re.match(password_pattern, password)
print("Is password strong?", bool(is_valid))
