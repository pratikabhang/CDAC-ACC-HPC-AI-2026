#include <iostream>
using namespace std;

class Box
{
private:
    int length;
    int width;
    int height;

public:
    Box()
    {
        this->length = 0;
        this->width = 0;
        this->height = 0;
    }

    Box(int length, int width, int height)
    {
        this->length = length;
        this->width = width;
        this->height = height;
    }

    int Volume()
    {
        return this->length * this->width * this->height;
    }

    void Display()
    {
        cout << "Length : " << this->length << endl;
        cout << "Width  : " << this->width << endl;
        cout << "Height : " << this->height << endl;
        cout << "Volume : " << this->Volume() << endl;
    }

    bool operator>(Box other)
    {
        return this->Volume() > other.Volume();
    }
};

int main()
{
    cout << endl;

    Box b1;

    cout << "Default Object b1:" << endl;
    b1.Display();

    cout << "\n------------------------" << endl;

    Box b2(10, 5, 4);

    cout << "Parameterized Object b2:" << endl;
    b2.Display();

    cout << "\n------------------------" << endl;

    int length;
    int width;
    int height;

    cout << "Enter Length, Width and Height for b1: ";
    cin >> length >> width >> height;

    b1 = Box(length, width, height);

    cout << "\nUser Input Object b1:" << endl;
    b1.Display();

    cout << "\n------------------------" << endl;

    cout << "Comparing b1 and b2:" << endl;

    if (b1 > b2)
    {
        cout << "Box b1 has greater volume." << endl;
    }
    else if (b2 > b1)
    {
        cout << "Box b2 has greater volume." << endl;
    }
    else
    {
        cout << "Both boxes have equal volume." << endl;
    }

    cout << "\n------------------------" << endl;

    return 0;
}