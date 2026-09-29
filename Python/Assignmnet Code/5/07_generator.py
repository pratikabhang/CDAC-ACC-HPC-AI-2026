def numbers(n):
    for i in range(1, n + 1):
        yield i

n = int(input("Enter a number: "))

for value in numbers(n):
    print(value)
