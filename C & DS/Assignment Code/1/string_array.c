/*
Question 2:
Create an array using String.
Populate the array using user input.
Display the stored strings.
*/

#include <stdio.h>

int main()
{
    char str[5][50];
    int i;

    printf("Enter 5 strings:\n");

    for (i = 0; i < 5; i++)
    {
        scanf("%49s", str[i]);
    }

    printf("\nStored Strings:\n");

    for (i = 0; i < 5; i++)
    {
        printf("%s\n", str[i]);
    }

    return 0;
}