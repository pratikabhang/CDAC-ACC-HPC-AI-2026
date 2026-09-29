#include <stdio.h>

int main()
{
    int arr[5];
    int *ptr1, *ptr2;
    int i;

    printf("Enter 5 elements:\n");

    for(i = 0; i < 5; i++)
    {
        scanf("%d", &arr[i]);
    }

    ptr1 = &arr[4];
    ptr2 = &arr[1];

    printf("\nAddress of ptr1 = %p\n", (void *)ptr1);
    printf("Address of ptr2 = %p\n", (void *)ptr2);

    printf("Difference = %ld\n", ptr1 - ptr2);

    return 0;
}