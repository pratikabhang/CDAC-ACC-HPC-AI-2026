def count_file():
    file_path_name = input("Enter file name or file path: ")

    with open(file_path_name, "r") as file:
        data = file.read()

    vowels = 0

    for char in data.lower():
        if char in "aeiou":
            vowels += 1

    print("Number of lines:", len(data.splitlines()))
    print("Number of words:", len(data.split()))
    print("Number of characters:", len(data))
    print("Number of vowels:", vowels)


count_file()