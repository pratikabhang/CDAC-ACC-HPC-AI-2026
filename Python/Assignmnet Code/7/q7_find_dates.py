import re

def find_dates(text="Today is 10-25-2023 and tomorrow is 11-01-2023."):
    print("Text:", text)

    match = re.search(r"\b\d{2}-\d{2}-\d{4}\b", text)

    if match:
        print("First date:", match.group())
    else:
        print("No date found.")


find_dates()