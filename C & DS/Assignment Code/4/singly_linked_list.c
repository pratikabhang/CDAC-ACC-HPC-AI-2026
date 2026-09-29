#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

int main()
{
    struct Node *head = NULL, *temp, *newnode;
    int n, i;

    printf("Enter number of nodes: ");
    scanf("%d", &n);

    for(i = 0; i < n; i++)
    {
        newnode = (struct Node *)malloc(sizeof(struct Node));

        printf("Enter data for node %d: ", i + 1);
        scanf("%d", &newnode->data);

        newnode->next = NULL;

        if(head == NULL)
        {
            head = newnode;
            temp = head;
        }
        else
        {
            temp->next = newnode;
            temp = newnode;
        }
    }

    printf("\nSingly Linked List:\n");

    temp = head;

    while(temp != NULL)
    {
        printf("%d", temp->data);

        if(temp->next != NULL)
            printf(" -> ");

        temp = temp->next;
    }

    printf(" -> NULL\n");

    return 0;
}