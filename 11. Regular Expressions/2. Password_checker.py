# Create a password checker-it should be
# atleast (1) 8 characters long, (2) contains any sort letter, numbers %@#$..(3) has to end with numbers etc

import re

# Pattern for exactly 8 characters
pattern = re.compile(r"^(?=.*[a-zA-Z])(?=.*[%@#$.])[\w%@#$.]{7}[0-9]$")

# Test passwords
password1 = "Abc@#$.1"  # Valid - 8 chars
password2 = "gdyhdgajsg66465465#$%#$6"  # Invalid - too long

# Use fullmatch, search, or match
check1 = pattern.fullmatch(password1)
check2 = pattern.fullmatch(password2)

print(f"Password 1: {check1}")  # Will show Match object
print(f"Password 2: {check2}")  # Will show None

# Better way to check
if pattern.fullmatch(password1):
    print("Password 1 is valid ✓")
else:
    print("Password 1 is invalid ✗")

if pattern.fullmatch(password2):
    print("Password 2 is valid ✓")
else:
    print("Password 2 is invalid ✗")
