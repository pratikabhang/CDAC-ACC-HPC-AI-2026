#include <stdio.h>

int main()
{
    int a = 10;
    int b = 20;

    int *const ptr = &a;

    printf("Value = %d\n", *ptr);

    *ptr = 30;

    printf("New Value = %d\n", *ptr);

    return 0;
}