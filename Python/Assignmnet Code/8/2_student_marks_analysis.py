def marks_report(marks):
    high = low = marks[0]
    for mark in marks:
        if mark > high:
            high = mark
        if mark < low:
            low = mark

    average = sum(marks) / len(marks)
    above = [mark for mark in marks if mark > average]

    groups = {
        "Distinction": 0,
        "First Class": 0,
        "Second Class": 0,
        "Fail": 0
    }

    for mark in marks:
        if mark >= 75:
            groups["Distinction"] += 1
        elif mark >= 60:
            groups["First Class"] += 1
        elif mark >= 50:
            groups["Second Class"] += 1
        else:
            groups["Fail"] += 1

    return high, low, average, above, groups


def main():
    marks = [float(x) for x in input("Enter marks separated by spaces: ").split()]

    high, low, average, above, groups = marks_report(marks)

    print("All marks:", marks)
    print("Highest:", high, "Lowest:", low, "Average:", round(average, 2))
    print("Above average:", above)
    print("Categories:", groups)

    print("Reverse:", end=" ")
    for i in range(len(marks) - 1, -1, -1):
        print(marks[i], end=" ")
    print()


main()