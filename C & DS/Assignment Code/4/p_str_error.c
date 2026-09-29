#include <stdio.h>
#include <string.h>
#include <errno.h>

int main()
{
    FILE *fp;

    char filename[50];

    printf("Enter file name: ");
    scanf("%s", filename);

    fp = fopen(filename, "r");

    if(fp == NULL)
    {
        perror("perror");
        printf("strerror: %s\n", strerror(errno));
    }
    else
    {
        printf("File opened successfully.\n");
        fclose(fp);
    }

    return 0;
}