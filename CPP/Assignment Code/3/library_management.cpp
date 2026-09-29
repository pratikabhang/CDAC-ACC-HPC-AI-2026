#include<iostream>
using namespace std;

class LibraryBook
{
    int bookId;
    char bookName[50];
    char authorName[50];
    float price;

public:

    void Accept()
    {
        cout<<"Enter Book ID: ";
        cin>>bookId;

        cout<<"Enter Book Name: ";
        cin>>bookName;

        cout<<"Enter Author Name: ";
        cin>>authorName;

        cout<<"Enter Price: ";
        cin>>price;
    }

    void Display()
    {
        cout<<"Book ID = "<<bookId<<endl;
        cout<<"Book Name = "<<bookName<<endl;
        cout<<"Author Name = "<<authorName<<endl;
        cout<<"Price = "<<price<<endl;

        price = price - (price * 10 / 100);

        cout<<"Price After 10% Discount = "<<price;
    }
};

int main()
{
    LibraryBook b;

    b.Accept();

    cout<<endl;

    b.Display();

    return 0;
}