import re


def validate_mobile(mobile):
    pattern = r"^[6-9]\d{9}$"

    if re.fullmatch(pattern, mobile):
        return "Valid"
    else:
        return "Invalid"


def validate_email(email):
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if re.fullmatch(pattern, email):
        return "Valid"
    else:
        return "Invalid"


def validate_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$"

    if re.fullmatch(pattern, password):
        return "Valid"
    else:
        return "Invalid"


def validate_pin(pin):
    pattern = r"^\d{6}$"

    if re.fullmatch(pattern, pin):
        return "Valid"
    else:
        return "Invalid"


def validate_username(username):
    pattern = r"^[A-Za-z][A-Za-z0-9_]{2,19}$"

    if re.fullmatch(pattern, username):
        return "Valid"
    else:
        return "Invalid"


def main():
    mobile = input("Enter mobile number: ")
    email = input("Enter email address: ")
    password = input("Enter password: ")
    pin = input("Enter PIN code: ")
    username = input("Enter username: ")

    print("Mobile number:", validate_mobile(mobile))
    print("Email address:", validate_email(email))
    print("Password:", validate_password(password))
    print("PIN code:", validate_pin(pin))
    print("Username:", validate_username(username))


main()