#include <stdio.h>

int main()
{
    int a = 10;

    int *ptr;
    int **dptr;

    ptr = &a;
    dptr = &ptr;

    printf("Value = %d\n", a);
    printf("Using Pointer = %d\n", *ptr);
    printf("Using Double Pointer = %d\n", **dptr);

    return 0;
}