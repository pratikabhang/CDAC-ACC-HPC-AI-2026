#include <iostream>
using namespace std;

int main()
{
    int n, i;
    int total = 0;
    float average;

    cout << "Enter number of subjects: ";
    cin >> n;

    int *marks = new int[n];

    for(i = 0; i < n; i++)
    {
        cout << "Enter marks: ";
        cin >> marks[i];
    }

    cout << "\nMarks are:\n";

    for(i = 0; i < n; i++)
    {
        cout << marks[i] << endl;
        total = total + marks[i];
    }

    average = (float)total / n;

    cout << "Total = " << total << endl;
    cout << "Average = " << average << endl;

    delete[] marks;

    return 0;
}