#include <iostream>
using namespace std;

namespace Student
{
    int RollNo;
    char Name[30];

    void Display()
    {
        cout << "Roll No = " << RollNo << endl;
        cout << "Name = " << Name;
    }
}

using namespace Student;

int main()
{
    cout << "Enter Roll No: ";
    cin >> RollNo;

    cout << "Enter Name: ";
    cin >> Name;

    Display();

    return 0;
}