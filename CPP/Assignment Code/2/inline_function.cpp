#include <iostream>
using namespace std;

inline int Square(int n)
{
    return n * n;
}

int main()
{
    int n, ans;

    cout << "Enter Number: ";
    cin >> n;

    ans = Square(n);

    cout << "Square = " << ans;

    return 0;
}