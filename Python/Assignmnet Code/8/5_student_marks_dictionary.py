def student_report(students):
    highest_average = 0
    highest_student = ""

    distinction = 0
    first_class = 0
    second_class = 0
    fail = 0

    for name, marks in students.items():
        total = sum(marks)
        average = total / 3

        print("\nName:", name)
        print("Marks:", marks)
        print("Total:", total)
        print("Average:", average)

        if average >= 75:
            grade = "Distinction"
            distinction += 1
        elif average >= 60:
            grade = "First Class"
            first_class += 1
        elif average >= 50:
            grade = "Second Class"
            second_class += 1
        else:
            grade = "Fail"
            fail += 1

        print("Grade:", grade)

        passed = True

        for mark in marks:
            if mark < 40:
                passed = False

        if passed:
            print("Passed in all subjects")

        if highest_student == "" or average > highest_average:
            highest_average = average
            highest_student = name

    print("\nStudent with highest average:", highest_student)
    print("Highest average:", highest_average)

    print("\nStudents in each grade:")
    print("Distinction:", distinction)
    print("First Class:", first_class)
    print("Second Class:", second_class)
    print("Fail:", fail)


def search_student(students):
    name = input("\nEnter student name to search: ")

    if name in students:
        print("Student found")
        print("Name:", name)
        print("Marks:", students[name])
    else:
        print("Student not found")


def main():
    n = int(input("Enter number of students: "))

    students = {}

    for i in range(n):
        name = input("Enter student name: ")

        marks = []

        for j in range(3):
            mark = float(input("Enter marks for subject " + str(j + 1) + ": "))
            marks.append(mark)

        students[name] = marks

    student_report(students)
    search_student(students)


main()