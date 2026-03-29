import re

# ----------------------------
# 1️⃣ Email Validation
# ----------------------------
def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

# ----------------------------
# 2️⃣ Phone Number Validation
# Supports: +91-9876543210, 09876543210, 9876543210
# ----------------------------
def is_valid_phone(phone):
    pattern = r"^(\+91[-\s]?|0)?[6-9]\d{9}$"
    return bool(re.match(pattern, phone))

# ----------------------------
# 3️⃣ Date Validation (dd/mm/yyyy)
# ----------------------------
def is_valid_date(date):
    pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}$"
    return bool(re.match(pattern, date))

# ----------------------------
# 4️⃣ Postal Code Validation (Indian PIN - 6 digits)
# ----------------------------
def is_valid_pin(pin):
    pattern = r"^[1-9][0-9]{5}$"
    return bool(re.match(pattern, pin))

# ----------------------------
# 5️⃣ Password Strength Validation
# Conditions: 8+ chars, 1 uppercase, 1 lowercase, 1 digit, 1 special char
# ----------------------------
def is_strong_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
    return bool(re.match(pattern, password))


# ----------------------------
# ✅ Test the validators
# ----------------------------

print("===== DATA VALIDATION EXAMPLES =====")

# Test emails
emails = ["test@example.com", "bad-email@", "name.surname@domain.co.in"]
for email in emails:
    print(f"Email: {email} --> {is_valid_email(email)}")

# Test phones
phones = ["+91-9876543210", "09876543210", "9876543210", "1234567890"]
for phone in phones:
    print(f"Phone: {phone} --> {is_valid_phone(phone)}")

# Test dates
dates = ["25/07/2025", "31/02/2024", "01/13/2024", "1/1/2024"]
for date in dates:
    print(f"Date: {date} --> {is_valid_date(date)}")

# Test PINs
pins = ["110001", "000001", "1234567"]
for pin in pins:
    print(f"PIN: {pin} --> {is_valid_pin(pin)}")

# Test passwords
passwords = ["Password123!", "weakpass", "Passw0rd", "P@ss!2"]
for pwd in passwords:
    print(f"Password: {pwd} --> {is_strong_password(pwd)}")
