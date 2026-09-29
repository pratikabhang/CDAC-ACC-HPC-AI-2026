def employee_report(employees):
    print("All employees:")

    for employee in employees:
        print(employee)

    highest = employees[0]
    total = 0

    for employee in employees:
        total += employee[2]

        if employee[2] > highest[2]:
            highest = employee

    average = total / len(employees)

    print("Employee receiving highest salary:", highest)
    print("Average salary:", average)

    print("Employees whose salary is greater than average:")

    for employee in employees:
        if employee[2] > average:
            print(employee)

    below_30000 = 0
    between_30000_60000 = 0
    above_60000 = 0

    for employee in employees:
        if employee[2] < 30000:
            below_30000 += 1
        elif employee[2] <= 60000:
            between_30000_60000 += 1
        else:
            above_60000 += 1

    print("Below 30,000:", below_30000)
    print("30,000 to 60,000:", between_30000_60000)
    print("Above 60,000:", above_60000)


def search_employee(employees):
    employee_id = int(input("Enter employee ID to search: "))

    for employee in employees:
        if employee[0] == employee_id:
            print("Employee found:", employee)
            return

    print("Employee not found")


def main():
    n = int(input("Enter number of employees: "))

    employee_list = []

    for i in range(n):
        employee_id = int(input("Enter employee ID: "))
        employee_name = input("Enter employee name: ")
        salary = float(input("Enter salary: "))

        employee_list.append((employee_id, employee_name, salary))

    employees = tuple(employee_list)

    employee_report(employees)
    search_employee(employees)


main()