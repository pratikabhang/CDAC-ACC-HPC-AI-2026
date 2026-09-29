class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print("Name:", self.name)
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)


class Manager(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, salary)
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        print("\nEmployees Managed:")
        for employee in self.employees:
            print(employee.name)


employee1 = Employee("Rahul", "E101", 30000)
employee2 = Employee("Priya", "E102", 35000)

manager = Manager("Pratik", "M101", 50000)

manager.add_employee(employee1)
manager.add_employee(employee2)

manager.display_info()
manager.display_employees()