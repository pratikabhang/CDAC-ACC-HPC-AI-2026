def menu():
    numbers = []

    while True:
        print("\n1. Insert")
        print("2. Delete")
        print("3. Search")
        print("4. Largest and Smallest")
        print("5. Reverse")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            numbers.append(int(input("Enter number: ")))
        elif choice == "2":
            number = int(input("Enter number: "))
            if number in numbers:
                numbers.remove(number)
            else:
                print("Number not found")
        elif choice == "3":
            number = int(input("Enter number: "))
            print("Found:", number in numbers)
        elif choice == "4" and numbers:
            print("Largest:", max(numbers))
            print("Smallest:", min(numbers))
        elif choice == "5":
            print("Reverse:", numbers[::-1])
        elif choice == "6":
            break

menu()
