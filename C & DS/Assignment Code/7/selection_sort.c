#include <stdio.h>

int main()
{
    int a[100], n, i, j, min, temp;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter elements:\n");

    for(i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    for(i = 0; i < n - 1; i++)
    {
        min = i;

        for(j = i + 1; j < n; j++)
        {
            if(a[j] < a[min])
            {
                min = j;
            }
        }

        temp = a[i];
        a[i] = a[min];
        a[min] = temp;
    }

    printf("Sorted Array:\n");

    for(i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }

    return 0;
}