#include <stdio.h>
#include <stdlib.h>

int Compare(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

int main()
{
    int n, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    int a[n];

    printf("Enter elements:\n");

    for(i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }

    qsort(a, n, sizeof(int), Compare);

    printf("Sorted Array:\n");

    for(i = 0; i < n; i++)
    {
        printf("%d ", a[i]);
    }

    return 0;
}