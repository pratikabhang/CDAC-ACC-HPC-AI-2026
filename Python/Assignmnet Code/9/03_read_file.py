filename = input("Enter the filename: ")

try:
    file = open(filename, "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("Error: File does not exist.")

except PermissionError:
    print("Error: You do not have permission to open this file.")