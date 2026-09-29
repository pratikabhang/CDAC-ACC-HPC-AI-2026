#include <stdio.h>

int main()
{
    int a, b;
    float implicitCast, explicitCast;

    printf("Enter two integers: ");
    scanf("%d%d", &a, &b);

    implicitCast = a + b;
    explicitCast = (float)a / b;

    printf("Implicit Casting Result: %.2f\n", implicitCast);
    printf("Explicit Casting Result: %.2f\n", explicitCast);

    return 0;
}