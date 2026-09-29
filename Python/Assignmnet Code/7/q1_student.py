class Student:
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id

    def display_info(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Student ID:", self.student_id)

    def is_eligible_to_vote(self):
        return self.age >= 18


name = input("Enter name: ")
age = int(input("Enter age: "))
student_id = input("Enter student ID: ")

student = Student(name, age, student_id)

student.display_info()
print("Eligible to vote:", student.is_eligible_to_vote())