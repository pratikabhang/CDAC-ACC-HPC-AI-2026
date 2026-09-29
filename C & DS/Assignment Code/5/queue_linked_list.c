#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

int main()
{
    struct Node *front = NULL;
    struct Node *rear = NULL;
    struct Node *newnode;
    struct Node *temp;

    int n, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    for(i = 0; i < n; i++)
    {
        newnode = (struct Node *)malloc(sizeof(struct Node));

        printf("Enter element: ");
        scanf("%d", &newnode->data);

        newnode->next = NULL;

        if(front == NULL)
        {
            front = rear = newnode;
        }
        else
        {
            rear->next = newnode;
            rear = newnode;
        }
    }

    printf("\nQueue Elements:\n");

    temp = front;

    while(temp != NULL)
    {
        printf("%d\n", temp->data);
        temp = temp->next;
    }

    return 0;
}