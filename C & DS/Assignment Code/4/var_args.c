#include <stdio.h>
#include <stdarg.h>

int sum(int n, ...)
{
    int i, total = 0;
    va_list args;

    va_start(args, n);

    for(i = 0; i < n; i++)
    {
        total += va_arg(args, int);
    }

    va_end(args);

    return total;
}

int main()
{
    int n, i, num;

    printf("Enter number of values: ");
    scanf("%d", &n);

    int arr[n];

    printf("Enter values:\n");
    for(i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }

    switch(n)
    {
        case 1:
            printf("Sum = %d", sum(1, arr[0]));
            break;
        case 2:
            printf("Sum = %d", sum(2, arr[0], arr[1]));
            break;
        case 3:
            printf("Sum = %d", sum(3, arr[0], arr[1], arr[2]));
            break;
        case 4:
            printf("Sum = %d", sum(4, arr[0], arr[1], arr[2], arr[3]));
            break;
        case 5:
            printf("Sum = %d", sum(5, arr[0], arr[1], arr[2], arr[3], arr[4]));
            break;
        default:
            printf("Enter up to 5 values.");
    }

    return 0;
}