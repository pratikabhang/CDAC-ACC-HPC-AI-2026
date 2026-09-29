#include <iostream>
using namespace std;

namespace Math
{
    void Square(int n)
    {
        cout << "Square = " << n * n;
    }
}

int main()
{
    int num;

    cout << "Enter a number: ";
    cin >> num;

    Math::Square(num);

    return 0;
}