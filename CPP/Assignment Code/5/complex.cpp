#include <iostream>
using namespace std;

class Complex
{
private:
    int real;
    int imag;

public:
    Complex()
    {
        this->real = 0;
        this->imag = 0;
    }

    Complex(int real, int imag)
    {
        this->real = real;
        this->imag = imag;
    }

    void Display()
    {
        cout << " " << this->real << " + " << this->imag << "i";
    }

    Complex operator+(Complex other)
    {
        Complex temp;

        temp.real = this->real + other.real;
        temp.imag = this->imag + other.imag;

        return temp;
    }

    Complex operator-(Complex other)
    {
        Complex temp;

        temp.real = this->real - other.real;
        temp.imag = this->imag - other.imag;

        return temp;
    }

    Complex operator++()
    {
        this->real = this->real + 1;
        this->imag = this->imag + 1;

        return *this;
    }

    Complex operator++(int)
    {
        Complex temp = *this;

        this->real = this->real + 1;
        this->imag = this->imag + 1;

        return temp;
    }

    Complex operator--()
    {
        this->real = this->real - 1;
        this->imag = this->imag - 1;

        return *this;
    }

    Complex operator--(int)
    {
        Complex temp = *this;

        this->real = this->real - 1;
        this->imag = this->imag - 1;

        return temp;
    }

    friend ostream &operator<<(ostream &os, Complex c)
    {
        os << c.real << " + " << c.imag << "i";
        return os;
    }

    friend istream &operator>>(istream &is, Complex &c)
    {
        is >> c.real >> c.imag;
        return is;
    }
};

int main()
{
    cout << endl;

    Complex defaultObj;
    Complex c1, c2;

    defaultObj = Complex();

    cout << "Default Object:";
    defaultObj.Display();

    cout << "\n------------------------" << endl;

    c1 = Complex(10, 20);

    cout << "Object 1 (c1):";
    c1.Display();

    cout << "\n------------------------" << endl;

    c2 = Complex(5, 8);

    cout << "Object 2 (c2):";
    c2.Display();

    cout << "\n------------------------" << endl;

    Complex add = c1 + c2;

    cout << "Addition (c1 + c2):";
    add.Display();

    cout << "\n------------------------" << endl;

    Complex sub = c1 - c2;

    cout << "Subtraction (c1 - c2):";
    sub.Display();

    cout << "\n------------------------" << endl;

    Complex preInc = ++c1;

    cout << "Prefix Increment (++c1):";
    preInc.Display();

    cout << "\n------------------------" << endl;

    Complex postInc = c2++;

    cout << "Postfix Increment (c2++):";
    postInc.Display();

    cout << endl;

    cout << "After Postfix Increment c2:";
    c2.Display();

    cout << "\n------------------------" << endl;

    Complex preDec = --c1;

    cout << "Prefix Decrement (--c1):";
    preDec.Display();

    cout << "\n------------------------" << endl;

    Complex postDec = c2--;

    cout << "Postfix Decrement (c2--):";
    postDec.Display();

    cout << endl;

    cout << "After Postfix Decrement c2:";
    c2.Display();

    cout << "\n------------------------" << endl;

    cout << "Using ostream (<<): ";
    cout << c1;

    cout << "\n------------------------" << endl;

    cout << "Enter real and imaginary values for c1: ";
    cin >> c1;

    cout << "Using istream (>>): ";
    cout << c1;

    cout << endl;

    return 0;
}