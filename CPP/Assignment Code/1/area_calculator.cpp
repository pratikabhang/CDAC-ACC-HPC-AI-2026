#include <iostream>
using namespace std;

namespace Rectangle
{
    void Area(float length, float width)
    {
        cout << "Area of Rectangle = " << length * width;
    }
}

namespace Circle
{
    void Area(float radius)
    {
        cout << "Area of Circle = " << 3.14 * radius * radius;
    }
}

int main()
{
    int choice;
    float length, width, radius;

    cout << "1. Rectangle";
    cout << "\n2. Circle";
    cout << "\nEnter your choice: ";
    cin >> choice;

    switch (choice)
    {
    case 1:
        cout << "Enter length: ";
        cin >> length;

        cout << "Enter width: ";
        cin >> width;

        Rectangle::Area(length, width);
        break;

    case 2:
        cout << "Enter radius: ";
        cin >> radius;

        Circle::Area(radius);
        break;

    default:
        cout << "Invalid choice";
    }

    return 0;
}