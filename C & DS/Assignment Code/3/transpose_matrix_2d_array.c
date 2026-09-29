#include <stdio.h>

int main()
{
    int row, col, i, j;

    printf("Enter rows and columns: ");
    scanf("%d%d", &row, &col);

    int mat[row][col], trans[col][row];

    printf("Enter matrix elements:\n");
    for(i = 0; i < row; i++)
    {
        for(j = 0; j < col; j++)
        {
            scanf("%d", &mat[i][j]);
        }
    }

    for(i = 0; i < row; i++)
    {
        for(j = 0; j < col; j++)
        {
            trans[j][i] = mat[i][j];
        }
    }

    printf("Transpose Matrix:\n");
    for(i = 0; i < col; i++)
    {
        for(j = 0; j < row; j++)
        {
            printf("%d ", trans[i][j]);
        }
        printf("\n");
    }

    return 0;
}