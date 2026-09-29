#include<iostream>
using namespace std;

void Swap(int &a,int &b)
{
    int t;

    t = a;
    a = b;
    b = t;
}

int main()
{
    int a,b;

    cout<<"Enter Two Numbers: ";
    cin>>a>>b;

    Swap(a,b);

    cout<<"After Swap"<<endl;
    cout<<"a = "<<a<<endl;
    cout<<"b = "<<b;

    return 0;
}