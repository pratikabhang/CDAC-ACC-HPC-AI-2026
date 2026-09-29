print('by default')

numbers = [12, 45, 2, 99, 23, 8]

even_list = []
odd_list = []

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print('original list:', numbers)
print('even numbers:', even_list)
print('odd numbers:', odd_list)


print('\nby user')

numbers = []
even_list = []
odd_list = []

n = int(input("enter no. of elements: "))

for i in range(n):
    num = int(input(f"enter element {i+1}: "))
    numbers.append(num)

for num in numbers:
    if num % 2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print('original list:', numbers)
print('even numbers:', even_list)
print('odd numbers:', odd_list)