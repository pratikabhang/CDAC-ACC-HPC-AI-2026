def menu():
    my_set = set()
    my_dict = {}

    while True:
        print("\n1. Add to Set")
        print("2. Add to Dictionary")
        print("3. Display Set")
        print("4. Display Dictionary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            value = input("Enter value: ")
            my_set.add(value)

        elif choice == "2":
            key = input("Enter key: ")
            value = input("Enter value: ")
            my_dict[key] = value

        elif choice == "3":
            print("Set:", my_set)

        elif choice == "4":
            print("Dictionary:", my_dict)

        elif choice == "5":
            break

        else:
            print("Invalid choice")

menu()
