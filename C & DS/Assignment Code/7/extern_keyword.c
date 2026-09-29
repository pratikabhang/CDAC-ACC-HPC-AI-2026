#include <stdio.h>

int a = 100;

void Display()
{
    extern int a;

    printf("Value = %d\n", a);
}

int main()
{
    Display();

    return 0;
}