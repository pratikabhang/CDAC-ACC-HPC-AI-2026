import csv

def write_csv(data):
    with open("people.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


name = input("Enter name: ")
age = input("Enter age: ")

data = [
    ["Name", "Age"],
    ["Pratik", 22],
    [name, age]
]

write_csv(data)

print("CSV file created successfully.")