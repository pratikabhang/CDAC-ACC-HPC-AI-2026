#include<iostream>
using namespace std;

class Complex
{
    int real,img;

public:

    void Accept()
    {
        cout<<"Enter Real Part: ";
        cin>>real;

        cout<<"Enter Imaginary Part: ";
        cin>>img;
    }

    void Display()
    {
        cout<<"Complex Number = "<<real<<" + "<<img<<"i"<<endl;
    }

    void AddComplexNumbers(Complex c1,Complex c2)
    {
        real = c1.real + c2.real;
        img = c1.img + c2.img;
    }
};

int main()
{
    Complex c1,c2,c3;

    cout<<"First Complex Number"<<endl;
    c1.Accept();

    cout<<"Second Complex Number"<<endl;
    c2.Accept();

    c3.AddComplexNumbers(c1,c2);

    cout<<"Result"<<endl;
    c3.Display();

    return 0;
}