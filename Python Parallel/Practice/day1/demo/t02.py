import pickle


class Employee:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id")
        self.name = kwargs.get("name")
        self.salary = kwargs.get("salary")

    def print(self):
        print(f"ID          : {self.id}")
        print(f"Name        : {self.name}")
        print(f"Salary      : {self.salary}")


def main_old():
    emp1 = Employee(id=1234, name="Ramesh", salary=59999)

    emp1_bytes = pickle.dumps(emp1)
    print(emp1_bytes)

    filename = "employee.bin"
    with open(filename, "wb") as file:
        pickle.dump(emp1, file)   
        print(f"Data saved in the file {filename}") 


def main():
    filename = "employee.bin"
    with open(filename, "rb") as f1:
        e1 = pickle.load(f1)
        e1.print()

if __name__ == "__main__":
    print("-"*80)
    main()
    print("-"*80)