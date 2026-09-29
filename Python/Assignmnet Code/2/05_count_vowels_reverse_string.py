print('by default')

text = "hello world"

rev_string = text[::-1]

print('string:', text)
print('reversed string:', rev_string)

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
counter = 0

for letter in rev_string:
    if letter in vowels:
        counter = counter + 1

print('vowels count:', counter)

print('\nby user')

text = input("enter a string: ")

rev_string = text[::-1]
counter = 0

for letter in rev_string:
    if letter in vowels:
        counter = counter + 1

print('string:', text)
print('reversed string:', rev_string)
print('vowels count:', counter)
