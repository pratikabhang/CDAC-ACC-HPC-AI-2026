#include <iostream>
#include <string>
using namespace std;

class Publisher
{
private:
    string pname;
    string city;
    string contact;

public:
    Publisher()
    {
        pname = "ABC";
        city = "Pune";
        contact = "9876543210";
    }

    Publisher(string p, string c, string con)
    {
        pname = p;
        city = c;
        contact = con;
    }

    void PublisherDisplay()
    {
        cout << pname << " " << city << " " << contact;
    }
};

class Book
{
private:
    int bid;
    string bname;
    float price;
    Publisher pub;

public:
    Book()
    {
        bid = 101;
        bname = "CPP";
        price = 500;
    }

    Book(int id, string bn, float pr, string p, string c, string con)
        : pub(p, c, con)
    {
        bid = id;
        bname = bn;
        price = pr;
    }

    void BookDisplay()
    {
        cout << bid << " " << bname << " " << price << " ";
        pub.PublisherDisplay();
        cout << endl;
    }
};

int main()
{
    cout << "\n";

    Book book1;
    cout << "Default:\n";
    book1.BookDisplay();
    cout << endl;

    Book book2(102, "Java", 700, "XYZ", "Mumbai", "9876543210");
    cout << "Parameterized:\n";
    book2.BookDisplay();
    cout << endl;

    int id;
    string bn;
    float pr;
    string p;
    string c;
    string con;

    cout << "Enter ID, Book Name, Price, Publisher Name, City, Contact: ";
    cin >> id >> bn >> pr >> p >> c >> con;

    Book book3(id, bn, pr, p, c, con);
    cout << "From User:\n";
    book3.BookDisplay();
    cout << "\n";

    return 0;
}