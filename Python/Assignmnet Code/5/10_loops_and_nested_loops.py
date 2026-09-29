def loops():
    n = int(input("Enter a number: "))

    print("Loop:")
    for i in range(1, n + 1):
        print(i)

    print("Nested Loop:")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

loops()
