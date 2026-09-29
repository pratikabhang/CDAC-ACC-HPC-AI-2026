#include <stdio.h>

#define MAX 10

int main()
{
    int queue[MAX];
    int front = 0;
    int rear = -1;
    int n, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    if(n > MAX)
    {
        printf("Queue Overflow");
        return 0;
    }

    for(i = 0; i < n; i++)
    {
        printf("Enter element: ");
        scanf("%d", &queue[++rear]);
    }

    printf("\nQueue Elements:\n");

    for(i = front; i <= rear; i++)
    {
        printf("%d\n", queue[i]);
    }

    return 0;
}