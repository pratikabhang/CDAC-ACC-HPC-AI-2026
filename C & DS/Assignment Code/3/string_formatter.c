#include <stdio.h>

int main()
{
    char name[50];
    int age;
    char str1[100];
    char str2[20];

    printf("Enter name: ");
    scanf("%s", name);

    printf("Enter age: ");
    scanf("%d", &age);

    sprintf(str1, "Name: %s Age: %d", name, age);
    snprintf(str2, sizeof(str2), "%s %d", name, age);

    printf("Using sprintf:\n%s\n", str1);
    printf("Using snprintf:\n%s\n", str2);

    return 0;
}