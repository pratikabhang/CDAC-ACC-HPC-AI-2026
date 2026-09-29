#include <stdio.h>

int main()
{
    FILE *fp;
    char name[50];
    char data[100];

    printf("Enter file name: ");
    scanf("%s", name);

    fp = fopen(name, "w");

    printf("Enter text: ");
    scanf(" %[^\n]", data);

    fprintf(fp, "%s", data);

    fclose(fp);

    fp = fopen(name, "r");

    fscanf(fp, " %[^\n]", data);

    printf("File Data: %s\n", data);

    fclose(fp);

    return 0;
}