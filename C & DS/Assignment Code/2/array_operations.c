/*
Question 3:
Write a program to calculate Sum, Average, Reverse, Ascending Order,
Descending Order, Minimum and Maximum of different integers using an array.
*/

#include <stdio.h>

int main()
{
    int n, i, j, temp;
    int arr[100];
    int sum = 0, min, max;
    float avg;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter %d integers:\n", n);

    for (i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
        sum += arr[i];
    }

    avg = (float)sum / n;
    min = max = arr[0];

    for (i = 1; i < n; i++)
    {
        if (arr[i] < min)
            min = arr[i];

        if (arr[i] > max)
            max = arr[i];
    }

    printf("\nSum = %d\n", sum);
    printf("Average = %.2f\n", avg);

    printf("Reverse Order: ");
    for (i = n - 1; i >= 0; i--)
        printf("%d ", arr[i]);

    for (i = 0; i < n - 1; i++)
    {
        for (j = i + 1; j < n; j++)
        {
            if (arr[i] > arr[j])
            {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }

    printf("\nAscending Order: ");
    for (i = 0; i < n; i++)
        printf("%d ", arr[i]);

    printf("\nDescending Order: ");
    for (i = n - 1; i >= 0; i--)
        printf("%d ", arr[i]);

    printf("\nMinimum = %d", min);
    printf("\nMaximum = %d\n", max);

    return 0;
}