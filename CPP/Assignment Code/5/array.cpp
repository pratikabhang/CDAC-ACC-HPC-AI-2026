#include <iostream>
using namespace std;

class Array
{
private:
    int *arr;
    int size;

public:
    Array()
    {
        this->size = 5;
        this->arr = new int[this->size];

        for (int i = 0; i < this->size; i++)
        {
            this->arr[i] = 0;
        }
    }

    Array(const Array &other)
    {
        this->size = other.size;
        this->arr = new int[this->size];

        for (int i = 0; i < this->size; i++)
        {
            this->arr[i] = other.arr[i];
        }
    }

    void Accept()
    {
        cout << "Enter 5 elements: ";

        for (int i = 0; i < this->size; i++)
        {
            cin >> this->arr[i];
        }
    }

    void Display()
    {
        for (int i = 0; i < this->size; i++)
        {
            cout << this->arr[i] << " ";
        }

        cout << endl;
    }

    void Merge(Array other)
    {
        for (int i = 0; i < this->size; i++)
        {
            cout << this->arr[i] << " ";
        }

        for (int i = 0; i < other.size; i++)
        {
            cout << other.arr[i] << " ";
        }

        cout << endl;
    }

    Array operator+(Array other)
    {
        Array temp;

        for (int i = 0; i < this->size; i++)
        {
            temp.arr[i] = this->arr[i] + other.arr[i];
        }

        return temp;
    }

    Array operator-(Array other)
    {
        Array temp;

        for (int i = 0; i < this->size; i++)
        {
            temp.arr[i] = this->arr[i] - other.arr[i];
        }

        return temp;
    }

    ~Array()
    {
        delete[] this->arr;
    }
};

int main()
{
    cout << endl;

    Array a1;
    Array a2;

    cout << "Array 1:" << endl;
    a1.Accept();

    cout << "Array 1 elements: ";
    a1.Display();

    cout << "\n------------------------" << endl;

    cout << "Array 2:" << endl;
    a2.Accept();

    cout << "Array 2 elements: ";
    a2.Display();

    cout << "\n------------------------" << endl;

    cout << "Merged Array: ";
    a1.Merge(a2);

    cout << "\n------------------------" << endl;

    Array a3 = a1 + a2;

    cout << "Addition (Array 1 + Array 2): ";
    a3.Display();

    cout << "\n------------------------" << endl;

    Array a4 = a1 - a2;

    cout << "Subtraction (Array 1 - Array 2): ";
    a4.Display();

    cout << "\n------------------------" << endl;

    Array a5 = a1;

    cout << "Copy Constructor Array: ";
    a5.Display();

    cout << "\n------------------------" << endl;

    return 0;
}