#include<iostream>
using namespace std;

int Maximum(int a,int b)
{
    if(a>b)
        return a;
    else
        return b;
}

int Maximum(int a,int b,int c)
{
    if(a>b && a>c)
        return a;
    else if(b>c)
        return b;
    else
        return c;
}

float Maximum(float a,float b)
{
    if(a>b)
        return a;
    else
        return b;
}

int main()
{
    int a,b,c;
    float x,y;

    cout<<"Enter Two Integers: ";
    cin>>a>>b;

    cout<<"Maximum = "<<Maximum(a,b)<<endl;

    cout<<"Enter Three Integers: ";
    cin>>a>>b>>c;

    cout<<"Maximum = "<<Maximum(a,b,c)<<endl;

    cout<<"Enter Two Float Numbers: ";
    cin>>x>>y;

    cout<<"Maximum = "<<Maximum(x,y);

    return 0;
}