#include <iostream>
using namespace std;

int main()
{
    int students, subjects, i, j;
    int total, highest = 0;
    float average;

    cout << "Enter number of students: ";
    cin >> students;

    cout << "Enter number of subjects: ";
    cin >> subjects;

    int **marks = new int*[students];

    for(i = 0; i < students; i++)
    {
        marks[i] = new int[subjects];
    }

    for(i = 0; i < students; i++)
    {
        cout << "Enter marks of Student " << i + 1 << endl;

        for(j = 0; j < subjects; j++)
        {
            cin >> marks[i][j];

            if(marks[i][j] > highest)
            {
                highest = marks[i][j];
            }
        }
    }

    cout << "\nMarks\n";

    for(i = 0; i < students; i++)
    {
        total = 0;

        cout << "Student " << i + 1 << ": ";

        for(j = 0; j < subjects; j++)
        {
            cout << marks[i][j] << " ";
            total = total + marks[i][j];
        }

        average = (float)total / subjects;

        cout << " Total = " << total;
        cout << " Average = " << average << endl;
    }

    cout << "\nHighest Mark = " << highest << endl;

    for(i = 0; i < students; i++)
    {
        delete[] marks[i];
    }

    delete[] marks;

    return 0;
}