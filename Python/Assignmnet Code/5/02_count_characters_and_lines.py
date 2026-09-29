def count_file():
    file_name = input("Enter file path name: ")

    with open(file_name, "r") as file:
        data = file.read()

    print("Number of characters:", len(data))
    print("Number of lines:", len(data.splitlines()))

count_file()
