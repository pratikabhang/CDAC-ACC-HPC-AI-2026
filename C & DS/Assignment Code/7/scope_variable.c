#include <stdio.h>

int a = 100;

void Display()
{
    printf("Global Variable = %d\n", a);
}

int main()
{
    int a = 50;

    printf("Local Variable = %d\n", a);

    Display();

    return 0;
}