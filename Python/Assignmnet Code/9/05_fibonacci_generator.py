def fibonacci_gen(limit):
    a = 0
    b = 1

    while a <= limit:
        yield a
        a, b = b, a + b


limit = int(input("Enter the limit: "))

for number in fibonacci_gen(limit):
    print(number)