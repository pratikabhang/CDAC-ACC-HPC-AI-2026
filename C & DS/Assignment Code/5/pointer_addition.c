#include <stdio.h>

int main()
{
    int arr[5];
    int *ptr;
    int i;

    printf("Enter 5 elements:\n");

    for(i = 0; i < 5; i++)
    {
        scanf("%d", &arr[i]);
    }

    ptr = arr;

    printf("\nArray Elements using Pointer Addition:\n");

    for(i = 0; i < 5; i++)
    {
        printf("%d ", *(ptr + i));
    }

    return 0;
}