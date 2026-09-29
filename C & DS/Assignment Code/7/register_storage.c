#include <stdio.h>

int main()
{
    register int i;

    for(i = 1; i <= 5; i++)
    {
        printf("%d\n", i);
    }

    return 0;
}