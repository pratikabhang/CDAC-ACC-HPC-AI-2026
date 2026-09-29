#include <iostream>
#include <stdexcept>
using namespace std;

int main()
{
    int arr[] = {43, 54, 76, 23, 65, 2, 45, 56, 22, 5};
    int index;

    try
    {
        cout << "\n\tEnter The Index Number: ";
        cin >> index;

        if (index < 0 || index >= 10)
            throw out_of_range("Invalid Array Index");

        cout << "\n\tValue At " << index << " Is " << arr[index];
    }
    catch (const out_of_range &e)
    {
        cout << "\n\tERROR : " << e.what();
    }

    cout << "\n\n\n";
    return 0;
}