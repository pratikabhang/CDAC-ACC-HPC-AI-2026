def anonymous_function():
    number = int(input("Enter a number: "))

    square = lambda x: x * x

    print("Square:", square(number))

anonymous_function()
