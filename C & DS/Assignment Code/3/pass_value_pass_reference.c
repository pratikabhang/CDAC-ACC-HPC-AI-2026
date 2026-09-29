#include <stdio.h>

void passValue(int num)
{
    num = num + 10;
    printf("Inside Pass by Value: %d\n", num);
}

void passReference(int *ptr)
{
    *ptr = *ptr + 10;
    printf("Inside Pass by Reference: %d\n", *ptr);
}

int main()
{
    int num;

    printf("Enter a number: ");
    scanf("%d", &num);

    passValue(num);
    printf("After Pass by Value: %d\n", num);

    passReference(&num);
    printf("After Pass by Reference: %d\n", num);

    return 0;
}