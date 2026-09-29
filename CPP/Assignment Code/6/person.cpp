#include <iostream>
#include <string>

using namespace std;

class Person
{
protected:
    int age;
    string name;

public:
    Person()
    {
        age = 0;
        name = "";
    }

    void Accept()
    {
        cout << "Enter name: ";
        cin >> name;

        cout << "Enter age: ";
        cin >> age;
    }

    void Display()
    {
        cout << "\n--- Person Details ---" << endl;
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

class Student : public Person
{
private:
    int rno;
    float percentage;

public:
    Student() : Person()
    {
        rno = 0;
        percentage = 0.0;
    }

    void Accept()
    {
        Person::Accept();

        cout << "Enter Roll Number: ";
        cin >> rno;

        cout << "Enter Percentage: ";
        cin >> percentage;
    }

    void Display()
    {
        Person::Display();

        cout << "Roll Number: " << rno << endl;
        cout << "Percentage: " << percentage << "%" << endl;
    }
};

int main()
{
    Student s;

    cout << "--- Enter Student Details ---" << endl;

    s.Accept();

    cout << "\n--- Student Details ---" << endl;

    s.Display();

    return 0;
}