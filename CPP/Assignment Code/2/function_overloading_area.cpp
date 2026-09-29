#include<iostream>
using namespace std;

void Area(int r, float &a, float &c)
{
    a = 3.14 * r * r;
    c = 2 * 3.14 * r;
}

int main()
{
    int r;
    float a, c;

    cout<<"Enter Radius: ";
    cin>>r;

    Area(r, a, c);

    cout<<"Area = "<<a<<endl;
    cout<<"Circumference = "<<c;

    return 0;
}