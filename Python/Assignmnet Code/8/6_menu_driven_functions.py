def check_prime():
    number = int(input("Enter a number: "))

    if number < 2:
        print("Not a Prime Number")
    else:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                print("Not a Prime Number")
                return

        print("Prime Number")


def check_palindrome():
    text = input("Enter a string: ")

    if text == text[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")


def find_factorial():
    number = int(input("Enter a number: "))

    if number < 0:
        print("Factorial is not defined for negative numbers")
    else:
        factorial = 1

        for i in range(1, number + 1):
            factorial *= i

        print("Factorial:", factorial)


def generate_fibonacci():
    n = int(input("Enter number of terms: "))

    first = 0
    second = 1

    print("Fibonacci Series:")

    for i in range(n):
        print(first, end=" ")
        first, second = second, first + second

    print()


def main():
    while True:
        print("\n1. Check Prime Number")
        print("2. Check Palindrome")
        print("3. Find Factorial")
        print("4. Generate Fibonacci Series")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            check_prime()

        elif choice == "2":
            check_palindrome()

        elif choice == "3":
            find_factorial()

        elif choice == "4":
            generate_fibonacci()

        elif choice == "5":
            print("Program Ended")
            break

        else:
            print("Invalid Choice")

main()