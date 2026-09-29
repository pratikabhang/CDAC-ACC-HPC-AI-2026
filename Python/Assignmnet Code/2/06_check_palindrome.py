print('by default')

word = "radar"

backward_word = word[::-1]

if word == backward_word:
    print(f"Yes, '{word}' is a palindrome!")
else:
    print(f"No, '{word}' is NOT a palindrome.")

print('\nby user')

word = input("enter a string: ")

backward_word = word[::-1]

if word == backward_word:
    print(f"Yes, '{word}' is a palindrome!")
else:
    print(f"No, '{word}' is NOT a palindrome.")
