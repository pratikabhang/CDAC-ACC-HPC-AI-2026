import re

def remove_punctuation(text="Hello, World! How are you?"):
    return re.sub(r"[^\w\s]", "", text)

print("Default:", remove_punctuation())
text = input("Enter a string: ")
print("Result:", remove_punctuation(text))
