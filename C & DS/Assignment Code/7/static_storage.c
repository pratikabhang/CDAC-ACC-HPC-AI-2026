#include <stdio.h>

void Display()
{
    static int count = 0;

    count++;

    printf("Count = %d\n", count);
}

int main()
{
    Display();
    Display();
    Display();

    return 0;
}