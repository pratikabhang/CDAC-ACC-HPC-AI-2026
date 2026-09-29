#include <stdio.h>

int main()
{
    int a = 10;
    float b = 20.5;

    void *ptr;

    ptr = &a;
    printf("Integer = %d\n", *(int *)ptr);

    ptr = &b;
    printf("Float = %.2f\n", *(float *)ptr);

    return 0;
}