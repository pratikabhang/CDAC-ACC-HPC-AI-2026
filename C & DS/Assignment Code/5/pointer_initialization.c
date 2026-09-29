#include <stdio.h>

int main()
{
    int num;
    int *ptr;

    printf("Enter a number: ");
    scanf("%d", &num);

    ptr = &num;

    printf("\nValue of num = %d\n", num);
    printf("Address of num = %p\n", (void *)&num);

    printf("\nPointer stores address = %p\n", (void *)ptr);
    printf("Value using pointer = %d\n", *ptr);

    return 0;
}