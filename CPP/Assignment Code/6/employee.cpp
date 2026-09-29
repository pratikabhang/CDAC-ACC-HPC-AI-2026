#include <iostream>
#include <string>

using namespace std;

class Employee
{
protected:
    int employeeId;
    string employeeName;
    double basicSalary;

public:
    Employee()
    {
        employeeId = 0;
        employeeName = "";
        basicSalary = 0.0;
    }

    virtual void Accept()
    {
        cout << "Enter Employee ID: ";
        cin >> employeeId;

        cout << "Enter Employee Name: ";
        cin >> employeeName;

        cout << "Enter Basic Salary: ";
        cin >> basicSalary;
    }

    virtual void Display()
    {
        cout << "Employee ID: " << employeeId << endl;
        cout << "Employee Name: " << employeeName << endl;
        cout << "Basic Salary: " << basicSalary << endl;
    }

    virtual double calculateSalary() = 0;
};

class Manager : public Employee
{
private:
    double allowance;

public:
    Manager() : Employee()
    {
        allowance = 0.0;
    }

    void Accept() override
    {
        Employee::Accept();

        cout << "Enter Allowance: ";
        cin >> allowance;
    }

    void Display() override
    {
        cout << "\n--- Manager Details ---" << endl;

        Employee::Display();

        cout << "Allowance: " << allowance << endl;
    }

    double calculateSalary() override
    {
        return basicSalary + allowance;
    }
};

class Developer : public Employee
{
private:
    double bonus;

public:
    Developer() : Employee()
    {
        bonus = 0.0;
    }

    void Accept() override
    {
        Employee::Accept();

        cout << "Enter Bonus: ";
        cin >> bonus;
    }

    void Display() override
    {
        cout << "\n--- Developer Details ---" << endl;

        Employee::Display();

        cout << "Bonus: " << bonus << endl;
    }

    double calculateSalary() override
    {
        return basicSalary + bonus;
    }
};

class SalesEmployee : public Employee
{
private:
    double salesAmount;
    double commissionRate;

public:
    SalesEmployee() : Employee()
    {
        salesAmount = 0.0;
        commissionRate = 0.0;
    }

    void Accept() override
    {
        Employee::Accept();

        cout << "Enter Sales Amount: ";
        cin >> salesAmount;

        cout << "Enter Commission Rate: ";
        cin >> commissionRate;
    }

    void Display() override
    {
        cout << "\n--- Sales Employee Details ---" << endl;

        Employee::Display();

        cout << "Sales Amount: " << salesAmount << endl;
        cout << "Commission Rate: " << commissionRate << endl;
    }

    double calculateSalary() override
    {
        return basicSalary + (salesAmount * commissionRate);
    }
};

int main()
{
    int size;

    cout << "Enter size of employee array: ";
    cin >> size;

    if (size <= 0)
    {
        cout << "Invalid array size!" << endl;
        return 1;
    }

    Employee *employees[size];

    for (int i = 0; i < size; i++)
    {
        employees[i] = nullptr;
    }

    int count = 0;
    int ch;

    do
    {
        cout << "\n--- MENU ---" << endl;
        cout << "1. Add Manager" << endl;
        cout << "2. Add Developer" << endl;
        cout << "3. Add Sales Employee" << endl;
        cout << "4. Exit" << endl;

        cout << "Enter choice: ";
        cin >> ch;

        switch (ch)
        {
        case 1:

            if (count >= size)
            {
                cout << "Array is full!" << endl;
            }
            else
            {
                Manager m;

                m.Accept();

                employees[count] = &m;

                employees[count]->Display();

                cout << "Calculated Salary: "
                     << employees[count]->calculateSalary()
                     << endl;

                count++;
            }

            break;

        case 2:

            if (count >= size)
            {
                cout << "Array is full!" << endl;
            }
            else
            {
                Developer d;

                d.Accept();

                employees[count] = &d;

                employees[count]->Display();

                cout << "Calculated Salary: "
                     << employees[count]->calculateSalary()
                     << endl;

                count++;
            }

            break;

        case 3:

            if (count >= size)
            {
                cout << "Array is full!" << endl;
            }
            else
            {
                SalesEmployee s;

                s.Accept();

                employees[count] = &s;

                employees[count]->Display();

                cout << "Calculated Salary: "
                     << employees[count]->calculateSalary()
                     << endl;

                count++;
            }

            break;

        case 4:

            cout << "Bye" << endl;

            break;

        default:

            cout << "Invalid Choice!" << endl;
        }

    } while (ch != 4);

    return 0;
}