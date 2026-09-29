def tuple_operations(marks):
    print("Highest:", max(marks))
    print("Lowest:", min(marks))
    print("Average:", sum(marks) / len(marks))

    count = 0
    for mark in marks:
        if mark > 75:
            count += 1
    print("Above 75:", count)

    search = int(input("Enter mark to search: "))
    print("Found:", search in marks)

marks = []
for i in range(10):
    marks.append(int(input("Enter mark: ")))

tuple_operations(tuple(marks))
