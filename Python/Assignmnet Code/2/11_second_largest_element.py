print('by default')

numbers = [12, 45, 2, 99, 45, 23, 99, 8]

unique_numbers = list(set(numbers))
unique_numbers.sort()

second_largest = unique_numbers[-2]

print('original list:', numbers)
print('no duplicate list:', unique_numbers)
print('second largest element:', second_largest)


print('\nby user')

numbers = []

n = int(input("enter no. of elements: "))

for i in range(n):
    element = int(input(f"enter element {i+1}: "))
    numbers.append(element)

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    second_largest = unique_numbers[-2]

    print('original list:', numbers)
    print('no duplicate list:', unique_numbers)
    print('second largest element:', second_largest)
else:
    print('enter at least two different numbers.')