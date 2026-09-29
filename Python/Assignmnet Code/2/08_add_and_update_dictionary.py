print('by default')

students = {
    "pratik": 85,
    "ram": 72,
    "rohit": 64,
    "abhi": 82,
    "parth": 80
}
print('original dictionary:', students)

for name, mark in students.items():
    if mark > 75:
        print("Students with marks more than 75:",name,":",mark)

students["aditya"] = 90
students["ram"] = 78

print('updated dictionary:', students)