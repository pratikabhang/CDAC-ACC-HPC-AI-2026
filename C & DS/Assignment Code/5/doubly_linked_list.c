#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *prev;
    struct Node *next;
};

int main()
{
    struct Node *head = NULL;
    struct Node *temp = NULL;
    struct Node *newnode;
    int n, i;

    printf("Enter number of nodes: ");
    scanf("%d", &n);

    for(i = 0; i < n; i++)
    {
        newnode = (struct Node *)malloc(sizeof(struct Node));

        printf("Enter data: ");
        scanf("%d", &newnode->data);

        newnode->next = NULL;
        newnode->prev = temp;

        if(head == NULL)
        {
            head = newnode;
        }
        else
        {
            temp->next = newnode;
        }

        temp = newnode;
    }

    printf("\nDoubly Linked List:\n");

    temp = head;

    while(temp != NULL)
    {
        printf("%d", temp->data);

        if(temp->next != NULL)
        {
            printf(" <-> ");
        }

        temp = temp->next;
    }

    printf(" <-> NULL");

    return 0;
}