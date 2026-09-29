#include<iostream>
using namespace std;

class Date
{
    int day,month,year;

public:

    void Accept()
    {
        cout<<"Enter Day: ";
        cin>>day;

        cout<<"Enter Month: ";
        cin>>month;

        cout<<"Enter Year: ";
        cin>>year;
    }

    void Display()
    {
        cout<<"Date = "<<day<<"/"<<month<<"/"<<year<<endl;
    }

    void Display(char ch)
    {
        cout<<"Date = "<<day<<ch<<month<<ch<<year<<endl;
    }

    void CheckLeapYear()
    {
        if((year%400==0) || (year%4==0 && year%100!=0))
        {
            cout<<"Leap Year";
        }
        else
        {
            cout<<"Not Leap Year";
        }
    }
};

int main()
{
    Date d;

    d.Accept();

    cout<<endl;

    d.Display();

    d.Display('-');

    d.CheckLeapYear();

    return 0;
}