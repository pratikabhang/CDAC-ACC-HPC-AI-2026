// Slide reference: SLIDE 11 - Pthreads and OpenMP (also SLIDE 33 - Controlled Parallel-For Loops)
// Introductory example: OpenMP "parallel for"
// Splits the loop iterations across threads automatically.

#include <cstdio>

int main() {
    const int N = 10;
    int arr[N];

    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        arr[i] = i * i;
    }

    for (int i = 0; i < N; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
