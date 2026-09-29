/*
Question 2:
Ask the user for n terms.
Print the Fibonacci series using for loop and variables.
*/

#include <stdio.h>

int main()
{
    int n, i;
    int a = 0, b = 1, c;

    printf("Enter number of terms: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++)
    {
        printf("%d ", a);
        c = a + b;
        a = b;
        b = c;
    }

    return 0;
}