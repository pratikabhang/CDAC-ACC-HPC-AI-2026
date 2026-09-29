#include <iostream>
using namespace std;

namespace Calculator
{
    void Add(int a, int b)
    {
        cout << "Addition = " << a + b << endl;
    }

    void Subtract(int a, int b)
    {
        cout << "Subtraction = " << a - b << endl;
    }

    void Multiply(int a, int b)
    {
        cout << "Multiplication = " << a * b << endl;
    }

    void Divide(int a, int b)
    {
        if (b == 0)
            cout << "Division by zero is not possible";
        else
            cout << "Division = " << (float)a / b;
    }
}

int main()
{
    int a, b, choice;

    cout << "Enter first number: ";
    cin >> a;

    cout << "Enter second number: ";
    cin >> b;

    cout << "\n1. Addition";
    cout << "\n2. Subtraction";
    cout << "\n3. Multiplication";
    cout << "\n4. Division";
    cout << "\nEnter your choice: ";
    cin >> choice;

    switch (choice)
    {
    case 1:
        Calculator::Add(a, b);
        break;

    case 2:
        Calculator::Subtract(a, b);
        break;

    case 3:
        Calculator::Multiply(a, b);
        break;

    case 4:
        Calculator::Divide(a, b);
        break;

    default:
        cout << "Invalid choice";
    }

    return 0;
}