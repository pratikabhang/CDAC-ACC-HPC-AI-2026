def student_file():
    n = int(input("Enter number of students: "))

    with open("students.txt", "w") as file:
        for i in range(n):
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))
            file.write(name + "," + str(marks) + "\n")

    with open("students.txt", "r") as file:
        print("\nStudents scoring more than 60:")

        for line in file:
            name, marks = line.strip().split(",")

            if int(marks) > 60:
                print(name, marks)


student_file()