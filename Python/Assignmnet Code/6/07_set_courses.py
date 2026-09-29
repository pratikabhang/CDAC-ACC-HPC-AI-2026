python_students = set(input("Enter Python students names separated by space: ").split())
java_students = set(input("Enter Java students names separated by space: ").split())
all_students = set(input("Enter all students names separated by space: ").split())

print("Both courses:", python_students & java_students)
print("Only Python:", python_students - java_students)
print("Only Java:", java_students - python_students)
print("Either course:", python_students | java_students)
print("Neither course:", all_students - (python_students | java_students))