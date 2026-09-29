import re

def is_valid_phone(text):
    return bool(re.fullmatch(r"\d{10}", text))

text = input("Enter a phone number: ")

print(is_valid_phone(text))