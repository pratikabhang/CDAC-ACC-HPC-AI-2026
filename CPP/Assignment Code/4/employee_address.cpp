#include <iostream>
#include <string>
using namespace std;

class Address
{
private:
    string area;
    string city;
    int pin;

public:
    Address()
    {
        area = "cdac";
        city = "pune";
        pin = 411001;
    }

    Address(string a, string c, int p)
    {
        area = a;
        city = c;
        pin = p;
    }

    void AddressDisplay()
    {
        cout << area << " " << city << " " << pin;
    }
};

class Employee
{
private:
    int eid;
    string name;
    float salary;
    Address add;

public:
    Employee()
    {
        eid = 101;
        name = "pratik";
        salary = 90000;
    }

    Employee(int ei, string na, float sa, string area, string city, int pin)
        : add(area, city, pin)
    {
        eid = ei;
        name = na;
        salary = sa;
    }

    void EmployeeDisplay()
    {
        cout << eid << " " << name << " " << salary << " ";
        add.AddressDisplay();
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

    Employee emp2(102, "ram", 95000, "hinjewadi", "pune", 411057);
    cout << "Parameterized:\n";
    emp2.EmployeeDisplay();
    cout << endl;

    int ei;
    string na;
    float sa;
    string area;
    string city;
    int pin;

    cout << "Enter ID, Name, Salary, Area, City, Pin for Employee: ";
    cin >> ei >> na >> sa >> area >> city >> pin;

    Employee emp3(ei, na, sa, area, city, pin);
    cout << "From User:\n";
    emp3.EmployeeDisplay();
    cout << "\n";

    return 0;
}