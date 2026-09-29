def create_data_file():
    with open("data.txt", "w") as file:
        file.write("Python programming\nFile handling\nEnd of file")

def read_and_print_file():
    with open("data.txt", "r") as file:
        print(file.read())

create_data_file()
read_and_print_file()
