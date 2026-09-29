#include <stdio.h>

void Display()
{
    printf("Callback Function Called");
}

void Call(void (*ptr)())
{
    ptr();
}

int main()
{
    Call(Display);

    return 0;
}