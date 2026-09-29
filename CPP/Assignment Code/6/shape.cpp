#include <iostream>
#include <string>

using namespace std;

class Shape
{
protected:
    string shapeName;

public:
    Shape(string name)
    {
        shapeName = name;
    }

    void DisplayShape()
    {
        cout << "\n--- " << shapeName << " ---" << endl;
    }

    virtual void Accept() = 0;
    virtual void Area() = 0;
};

class Circle : public Shape
{
private:
    double radius;

public:
    Circle() : Shape("Circle")
    {
        radius = 0.0;
    }

    void Accept() override
    {
        cout << "Enter radius: ";
        cin >> radius;
    }

    void Area() override
    {
        cout << "Area of Circle: " << (3.14 * radius * radius) << endl;
    }
};

class Rectangle : public Shape
{
private:
    double length;
    double breadth;

public:
    Rectangle() : Shape("Rectangle")
    {
        length = 0.0;
        breadth = 0.0;
    }

    void Accept() override
    {
        cout << "Enter length: ";
        cin >> length;

        cout << "Enter breadth: ";
        cin >> breadth;
    }

    void Area() override
    {
        cout << "Area of Rectangle: " << (length * breadth) << endl;
    }
};

class Triangle : public Shape
{
private:
    double base;
    double height;

public:
    Triangle() : Shape("Triangle")
    {
        base = 0.0;
        height = 0.0;
    }

    void Accept() override
    {
        cout << "Enter base: ";
        cin >> base;

        cout << "Enter height: ";
        cin >> height;
    }

    void Area() override
    {
        cout << "Area of Triangle: " << (0.5 * base * height) << endl;
    }
};

int main()
{
    Circle c;
    Rectangle r;
    Triangle t;

    Shape *shapes[3];

    shapes[0] = &c;
    shapes[1] = &r;
    shapes[2] = &t;

    int ch;

    do
    {
        cout << "\n--- MENU ---" << endl;
        cout << "1. Circle" << endl;
        cout << "2. Rectangle" << endl;
        cout << "3. Triangle" << endl;
        cout << "4. Exit" << endl;

        cout << "Enter choice: ";
        cin >> ch;

        switch (ch)
        {
        case 1:
            shapes[0]->Accept();
            shapes[0]->DisplayShape();
            shapes[0]->Area();
            break;

        case 2:
            shapes[1]->Accept();
            shapes[1]->DisplayShape();
            shapes[1]->Area();
            break;

        case 3:
            shapes[2]->Accept();
            shapes[2]->DisplayShape();
            shapes[2]->Area();
            break;

        case 4:
            cout << "Bye" << endl;
            break;

        default:
            cout << "Invalid choice!" << endl;
        }

    } while (ch != 4);

    return 0;
}