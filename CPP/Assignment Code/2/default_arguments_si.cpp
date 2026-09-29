#include <iostream>
using namespace std;

float CalculateSI(float p, float t, float r = 8)
{
    return (p * t * r) / 100;
}

int main()
{
    float p, t, r;
    float ans1, ans2;

    cout << "Enter Principal: ";
    cin >> p;

    cout << "Enter Years: ";
    cin >> t;

    ans1 = CalculateSI(p, t);

    cout << "Simple Interest (Default Rate 8%) = " << ans1 << endl;

    cout << "Enter Rate: ";
    cin >> r;

    ans2 = CalculateSI(p, t, r);

    cout << "Simple Interest (Custom Rate) = " << ans2;

    return 0;
}