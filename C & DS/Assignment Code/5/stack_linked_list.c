#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

int main()
{
    struct Node *top = NULL;
    struct Node *newnode;
    int n, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    for(i = 0; i < n; i++)
    {
        newnode = (struct Node *)malloc(sizeof(struct Node));

        printf("Enter element: ");
        scanf("%d", &newnode->data);

        newnode->next = top;
        top = newnode;
    }

    printf("\nStack Elements:\n");

    while(top != NULL)
    {
        printf("%d\n", top->data);
        top = top->next;
    }

    return 0;
}