#include <stdio.h>

#define N 10

int main(void) {
    int a[N], b[N], result[N];
    int i;

    for (i = 0; i < N; i++) {
        a[i] = i + 1;
        b[i] = N - i;
    }

    #pragma acc data copyin(a[0:N], b[0:N]) copyout(result[0:N])
    {
        #pragma acc parallel loop
        for (i = 0; i < N; i++) {
            result[i] = a[i] + b[i];
        }
    }

    for (i = 0; i < N; i++) {
        printf("%d + %d = %d\n", a[i], b[i], result[i]);
    }

    return 0;
}
