#include <stdio.h>

int main()
{
    volatile int a;

    printf("Enter a number: ");
    scanf("%d", &a);

    printf("Value = %d", a);

    return 0;
}