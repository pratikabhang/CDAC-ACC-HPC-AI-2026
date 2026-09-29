#include <iostream>
#include <string>
using namespace std;

class Date
{
private:
    int day;
    int month;
    int year;

public:
    Date()
    {
        day = 21;
        month = 11;
        year = 2003;
    }

    Date(int d, int m, int y)
    {
        day = d;
        month = m;
        year = y;
    }

    void DateDisplay()
    {
        cout << " " << day << " - " << month << " - " << year;
    }
};

class Employee
{
private:
    int eid;
    string name;
    float salary;
    Date doj;

public:
    Employee()
    {
        eid = 101;
        name = "pratik";
        salary = 90000;
    }

    Employee(int ei, string na, float sa, int day, int month, int year)
        : doj(day, month, year)
    {
        eid = ei;
        name = na;
        salary = sa;
    }

    void EmployeeDisplay()
    {
        cout << eid << " " << name << " " << salary;
        doj.DateDisplay();
        cout << endl;
    }
};

int main()
{
    cout << "\n";

    Employee emp1;
    cout << "Default:\n";
    emp1.EmployeeDisplay();
    cout << endl;

    Employee emp2(102, "ram", 95000, 22, 7, 2026);
    cout << "Parameterized:\n";
    emp2.EmployeeDisplay();
    cout << endl;

    int ei;
    string na;
    float sa;
    int day;
    int month;
    int year;

    cout << "Enter ID, Name, Salary, Day, Month, Year for Employee: ";
    cin >> ei >> na >> sa >> day >> month >> year;

    Employee emp3(ei, na, sa, day, month, year);
    cout << "From User:\n";
    emp3.EmployeeDisplay();
    cout << "\n";

    return 0;
}