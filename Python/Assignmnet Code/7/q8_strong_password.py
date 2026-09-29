import re

def is_strong_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,}$"
    return bool(re.fullmatch(pattern, password))


password = input("Enter a password: ")

print(is_strong_password(password))