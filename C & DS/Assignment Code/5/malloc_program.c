#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *ptr;
    int n, i;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    ptr = (int *)malloc(n * sizeof(int));

    if(ptr == NULL)
    {
        printf("Memory allocation failed.");
        return 0;
    }

    printf("Enter %d elements:\n", n);

    for(i = 0; i < n; i++)
    {
        scanf("%d", &ptr[i]);
    }

    printf("\nElements are:\n");

    for(i = 0; i < n; i++)
    {
        printf("%d ", ptr[i]);
    }

    free(ptr);

    return 0;
}