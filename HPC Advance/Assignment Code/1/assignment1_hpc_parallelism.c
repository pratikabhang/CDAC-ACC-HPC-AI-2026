#include <stdio.h>
#include <omp.h>

int main(void)
{
    printf("Assignment 1 - HPC Parallelism Analysis\n");
    printf("Language: C + OpenMP\n\n");

    printf("Ex 1  : PARALLEL - independent writes to a and b.\n");
    printf("Ex 2  : NOT PARALLEL - b depends on a.\n");
    printf("Ex 3  : NOT PARALLEL - b reads a before a is assigned.\n");
    printf("Ex 4  : NOT PARALLEL - both statements write a.\n");
    printf("Ex 5  : PARALLEL - each iteration writes a different a[i].\n");
    printf("Ex 7  : PARALLEL - each iteration writes independent a[i], b[i].\n");
    printf("Ex 8  : PARALLEL WITH ORDERED REGIONS - each loop is parallel; keep loop order.\n");
    printf("Ex 9  : PARALLEL - each iteration updates only its own a[i].\n");
    printf("Ex 10 : NOT PARALLEL - a[i] depends on a[i-1].\n");
    printf("Ex 11 : PARTIAL - outer i parallel; inner j is sequential due to dependency.\n");
    printf("Ex 12 : PARTIAL - outer j sequential; inner i parallel for each j.\n");
    printf("Ex 13 : NOT PARALLEL FOR ORDERED OUTPUT - printf order is observable.\n");
    printf("Ex 14 : PARALLEL IF f(x) AND g(x) HAVE NO SIDE EFFECT CONFLICT.\n");
    printf("Ex 15 : NOT PARALLEL - iterations can read values written by other iterations.\n");
    printf("Ex 16 : NOT PARALLEL - a[i-1] creates a loop-carried dependency.\n");
    printf("Ex 17 : CONDITIONAL - depends on indexa[] and possible write conflicts.\n\n");

    /* Example OpenMP implementations for the independent loops. */
    {
        int a[100], b[100];

#pragma omp parallel for
        for (int i = 0; i < 100; i++)
            a[i] = i;

#pragma omp parallel for
        for (int i = 0; i < 100; i++)
            b[i] = 2 * i;

        printf("OpenMP example checks: a[10]=%d, b[10]=%d\n", a[10], b[10]);
    }

    return 0;
}
