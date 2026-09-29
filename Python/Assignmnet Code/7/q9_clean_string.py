import re

def clean_string(text="  hello   world. how are you? i am fine!  "):
    text = re.sub(r"\s+", " ", text).strip()
    return re.sub(r"(^|[.!?]\s+)([a-z])",
                  lambda m: m.group(1) + m.group(2).upper(), text)

print("Default:", clean_string())
text = input("Enter a string: ")
print("Cleaned:", clean_string(text))
