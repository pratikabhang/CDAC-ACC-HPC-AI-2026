import os

def create_file_directory():
    folder = input("Enter folder name: ")
    file_name = input("Enter file name: ")

    os.makedirs(folder, exist_ok=True)

    path = os.path.join(folder, file_name)

    with open(path, "w") as file:
        file.write("Hello")

    print("Directory created:", folder)
    print("File created:", path)

create_file_directory()
