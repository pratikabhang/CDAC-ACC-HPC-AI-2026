#include <stdio.h>

#define MAX 10

int main()
{
    int stack[MAX];
    int top = -1;
    int n, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    if(n > MAX)
    {
        printf("Stack Overflow");
        return 0;
    }

    for(i = 0; i < n; i++)
    {
        printf("Enter element: ");
        scanf("%d", &stack[++top]);
    }

    printf("\nStack Elements:\n");

    while(top != -1)
    {
        printf("%d\n", stack[top]);
        top--;
    }

    return 0;
}