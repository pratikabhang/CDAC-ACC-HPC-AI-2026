// Slide reference: SLIDE 11 - Pthreads and OpenMP
// Module 2: same sum as 14_sum_openmp.cpp, but with reduction(+:total)
// added. Each thread gets its own private copy of "total", accumulates
// into it independently, and OpenMP combines all the private copies with
// + once every thread finishes - no shared-write race, correct every time.

#include <cstdio>
#include <omp.h>

const int N = 2000000;

int main() {
    int arr[N];
    for (int i = 0; i < N; i++) arr[i] = 1;   // correct sum is exactly N

    long total = 0;

    #pragma omp parallel for reduction(+:total)
    for (int i = 0; i < N; i++) {
        total += arr[i];
    }

    printf("Threads used: %d\n", omp_get_max_threads());
    printf("Total sum (OpenMP, with reduction): %ld  (expected %d)\n", total, N);
    return 0;
}
