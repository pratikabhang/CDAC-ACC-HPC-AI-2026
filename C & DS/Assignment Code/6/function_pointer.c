#include <stdio.h>

int Add(int a, int b)
{
    return a + b;
}

int main()
{
    int (*ptr)(int, int);

    ptr = Add;

    printf("Sum = %d", ptr(10, 20));

    return 0;
}