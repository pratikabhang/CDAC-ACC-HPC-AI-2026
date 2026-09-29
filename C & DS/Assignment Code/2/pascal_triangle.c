/*
Question 1:
Ask the user for the number of levels.
Print Pascal Triangle using for loops and variables (avoid arrays).
*/

#include <stdio.h>

int main()
{
    int n, i, j, num;

    printf("Enter number of levels: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++)
    {
        num = 1;

        for (j = 0; j < n - i - 1; j++)
            printf(" ");

        for (j = 0; j <= i; j++)
        {
            printf("%d ", num);
            num = num * (i - j) / (j + 1);
        }

        printf("\n");
    }

    return 0;
}