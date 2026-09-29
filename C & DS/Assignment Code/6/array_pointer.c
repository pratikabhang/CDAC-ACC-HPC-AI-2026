#include <stdio.h>

int main()
{
    int a[5];
    int *ptr;
    int i;

    ptr = a;

    printf("Enter 5 elements:\n");

    for(i = 0; i < 5; i++)
    {
        scanf("%d", ptr + i);
    }

    printf("Elements are:\n");

    for(i = 0; i < 5; i++)
    {
        printf("%d ", *(ptr + i));
    }

    return 0;
}