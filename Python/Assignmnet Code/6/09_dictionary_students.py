students = {"Pratik": 80, "Prathmesh": 70}

while True:
    print("\n1. Add")
    print("2. Update")
    print("3. Delete")
    print("4. Search")
    print("5. Above 75")
    print("6. Highest")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        students[name] = marks

    elif choice == "2":
        name = input("Enter student name: ")

        if name in students:
            students[name] = int(input("Enter new marks: "))
        else:
            print("Student not found")

    elif choice == "3":
        name = input("Enter student name: ")

        if name in students:
            del students[name]
        else:
            print("Student not found")

    elif choice == "4":
        name = input("Enter student name: ")
        print("Found:", name in students)

    elif choice == "5":
        print("Students above 75:")

        for name, marks in students.items():
            if marks > 75:
                print(name, marks)

    elif choice == "6":
        if students:
            name = max(students, key=students.get)
            print("Highest:", name, students[name])

    elif choice == "7":
        print("Exit")
        break

    else:
        print("Invalid choice")