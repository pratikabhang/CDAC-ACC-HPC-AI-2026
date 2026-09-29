#include <iostream>
using namespace std;

namespace India
{
    void Currency()
    {
        cout << "Currency of India is Rupee (INR)";
    }
}

namespace USA
{
    void Currency()
    {
        cout << "Currency of USA is Dollar (USD)";
    }
}

int main()
{
    int choice;

    cout << "1. India";
    cout << "\n2. USA";
    cout << "\nEnter your choice: ";
    cin >> choice;

    switch (choice)
    {
    case 1:
        India::Currency();
        break;

    case 2:
        USA::Currency();
        break;

    default:
        cout << "Invalid choice";
    }

    return 0;
}