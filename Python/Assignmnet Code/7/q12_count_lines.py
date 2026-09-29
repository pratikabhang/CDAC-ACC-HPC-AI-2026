def count_lines(filename="data.txt"):
    with open(filename, "r") as file:
        return sum(1 for _ in file)

filename = input("Enter file name: ")
print("Total lines:", count_lines(filename))
