#include <iostream>
using namespace std;

int main()
{
    int products, months, i, j;

    cout << "Enter number of products: ";
    cin >> products;

    cout << "Enter number of months: ";
    cin >> months;

    int **sales = new int*[products];

    for(i = 0; i < products; i++)
    {
        sales[i] = new int[months];
    }

    for(i = 0; i < products; i++)
    {
        cout << "Enter sales of Product " << i + 1 << endl;

        for(j = 0; j < months; j++)
        {
            cin >> sales[i][j];
        }
    }

    cout << "\nSales Report\n";

    for(i = 0; i < products; i++)
    {
        int total = 0;

        cout << "Product " << i + 1 << ": ";

        for(j = 0; j < months; j++)
        {
            cout << sales[i][j] << " ";
            total = total + sales[i][j];
        }

        cout << " Total = " << total << endl;
    }

    cout << "\nTotal Sales of Each Month\n";

    for(j = 0; j < months; j++)
    {
        int total = 0;

        for(i = 0; i < products; i++)
        {
            total = total + sales[i][j];
        }

        cout << "Month " << j + 1 << " = " << total << endl;
    }

    int grandTotal = 0;

    for(i = 0; i < products; i++)
    {
        for(j = 0; j < months; j++)
        {
            grandTotal = grandTotal + sales[i][j];
        }
    }

    cout << "\nGrand Total = " << grandTotal << endl;

    for(i = 0; i < products; i++)
    {
        delete[] sales[i];
    }

    delete[] sales;

    return 0;
}