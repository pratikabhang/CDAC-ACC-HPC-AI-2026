def list_operations():
    numbers = []

    n = int(input("How many numbers do you want to enter? "))

    for i in range(n):
        number = int(input("Enter number: "))
        numbers.append(number)

    even = []
    odd = []

    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    print("Even numbers:", even)
    print("Odd numbers:", odd)
    print("Sum:", sum(numbers))
    print("Average:", sum(numbers) / len(numbers))
    print("Largest:", max(numbers))
    print("Smallest:", min(numbers))
    print("Without duplicates:", list(set(numbers)))


list_operations()