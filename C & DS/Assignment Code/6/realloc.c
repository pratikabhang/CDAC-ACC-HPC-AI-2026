#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, m, i;
    int *ptr;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    ptr = (int *)malloc(n * sizeof(int));

    printf("Enter elements:\n");

    for (i = 0; i < n; i++)
    {
        scanf("%d", &ptr[i]);
    }

    printf("Enter new size: ");
    scanf("%d", &m);

    ptr = (int *)realloc(ptr, m * sizeof(int));

    if (m > n)
    {
        printf("Enter new elements:\n");

        for (i = n; i < m; i++)
        {
            scanf("%d", &ptr[i]);
        }
    }

    printf("Elements are:\n");

    for (i = 0; i < m; i++)
    {
        printf("%d ", ptr[i]);
    }

    free(ptr);

    return 0;
}