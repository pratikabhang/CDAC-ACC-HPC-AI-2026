#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *ptr;

    ptr = (int *)malloc(sizeof(int));

    if (ptr == NULL)
    {
        printf("Memory not allocated");
        return 0;
    }

    printf("Enter a number: ");
    scanf("%d", ptr);

    printf("Number = %d\n", *ptr);

    free(ptr);

    printf("Memory freed");

    return 0;
}