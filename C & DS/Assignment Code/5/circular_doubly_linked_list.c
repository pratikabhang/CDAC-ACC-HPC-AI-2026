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

        if(head == NULL)
        {
            head = newnode;
            head->next = head;
            head->prev = head;
            temp = head;
        }
        else
        {
            newnode->next = head;
            newnode->prev = temp;
            temp->next = newnode;
            head->prev = newnode;
            temp = newnode;
        }
    }

    printf("\nCircular Doubly Linked List:\n");

    temp = head;

    for(i = 0; i < n; i++)
    {
        printf("%d", temp->data);

        if(i != n - 1)
        {
            printf(" <-> ");
        }

        temp = temp->next;
    }

    printf(" <-> Back to Head");

    return 0;
}