#include<iostream>
using namespace std;

class Box
{
    int length,width,height;

public:

    void Accept()
    {
        cout<<"Enter Length: ";
        cin>>length;

        cout<<"Enter Width: ";
        cin>>width;

        cout<<"Enter Height: ";
        cin>>height;
    }

    void Display()
    {
        cout<<"Length = "<<length<<endl;
        cout<<"Width = "<<width<<endl;
        cout<<"Height = "<<height<<endl;
    }

    void CalculateVolume()
    {
        int volume;

        volume = length * width * height;

        cout<<"Volume = "<<volume;
    }
};

int main()
{
    Box b;

    b.Accept();

    cout<<endl;

    b.Display();

    b.CalculateVolume();

    return 0;
}