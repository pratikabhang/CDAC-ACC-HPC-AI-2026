sentence = input("Enter a sentence: ")

vowels = 0
digits = 0
spaces = 0

for char in sentence.lower():
    if char in "aeiou":
        vowels += 1
    if char.isdigit():
        digits += 1
    if char == " ":
        spaces += 1

print("Vowels:", vowels)
print("Digits:", digits)
print("Spaces:", spaces)
print("Words:", len(sentence.split()))
print("Reverse:", sentence[::-1])

text = sentence.replace(" ", "").lower()
print("Palindrome:", text == text[::-1])
