import pickle


class Employee:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.salary = kwargs.get("salary")

    def print(self):
        print("I am doing some malicious code execution here...")
        print("I could be reading some sensitive data...")
        print("I might be reading your emails...")
        print(f"ID          : {self.id}")
        print(f"Name        : {self.name}")
        print(f"Salary      : {self.salary}")


def main():
    emp1 = Employee(id=1234, name="Ramesh", salary=59999)

    filename = "employee.bin"
    with open(filename, "wb") as file:
        pickle.dump(emp1, file)   
        print(f"Data saved in the file {filename}") 


if __name__ == "__main__":
    print("-"*80)
    main()
    print("-"*80)