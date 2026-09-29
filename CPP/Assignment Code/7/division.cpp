#include <iostream>
#include <exception>
using namespace std;

class DivisionByZeroException : public exception
{
public:
    const char *what() const noexcept override
    {
        return "Division by zero is not allowed";
    }
};

int main()
{
    int numerator, denominator;

    cout << "\nEnter Numerator and Denominator: ";
    cin >> numerator >> denominator;

    try
    {
        if (denominator == 0)
            throw DivisionByZeroException();

        cout << "\nResult: " << numerator / denominator << endl;
    }
    catch (const DivisionByZeroException &e)
    {
        cout << "\nError: " << e.what() << endl;
    }
    catch (const exception &e)
    {
        cout << "\nError: " << e.what() << endl;
    }

    return 0;
}