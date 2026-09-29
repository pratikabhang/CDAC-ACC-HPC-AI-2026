#include <stdio.h>

void QuickSort(int a[], int first, int last)
{
    int i, j, pivot, temp;

    if(first < last)
    {
        pivot = first;
        i = first;
        j = last;

        while(i < j)
        {
            while(a[i] <= a[pivot] && i < last)
                i++;

            while(a[j] > a[pivot])
                j--;

            if(i < j)
            {
                temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }

        temp = a[pivot];
        a[pivot] = a[j];
        a[j] = temp;

        QuickSort(a, first, j - 1);
        QuickSort(a, j + 1, last);
    }
}

int main()
{
    int a[100], n, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter elements:\n");

    for(i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    QuickSort(a, 0, n - 1);

    printf("Sorted Array:\n");

    for(i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }

    return 0;
}