def is_palindrome(s):
    return s == s[::-1]

text1 = "madam"
if is_palindrome(text1):
    print(text1, "is Palindrome")
else:
    print(text1, "is Not Palindrome")