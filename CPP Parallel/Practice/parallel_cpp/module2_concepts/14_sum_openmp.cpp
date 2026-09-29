// Slide reference: SLIDE 11 - Pthreads and OpenMP (also SLIDE 44/45 -
// Race Conditions and Concurrency)
// Module 2: sum an array using OpenMP with a plain #pragma omp parallel
// for. Every thread reads, adds to, and writes back the same shared
// "total" with no synchronization - a classic race condition. See
// 14b_sum_openmp_reduction.cpp for the fix: adding reduction(+:total).
//
// Run this a few times: the result is wrong and varies. Each thread adds
// up its own chunk correctly, but writing that chunk's contribution into
// the shared "total" is itself an unsynchronized read-modify-write, so
// when multiple threads do it at once, some updates get overwritten and
// lost - only one thread's contribution (or a partial combination of a
// couple) survives instead of all of them.

#include <cstdio>
#include <omp.h>

const int N = 2000000;

int main() {
    int arr[N];
    for (int i = 0; i < N; i++) arr[i] = 1;   // correct sum is exactly N

    long total = 0;

    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        total += arr[i];   // read-modify-write on a SHARED variable: a race
    }

    printf("Threads used: %d\n", omp_get_max_threads());
    printf("Total sum (OpenMP, no reduction): %ld  (expected %d)\n", total, N);
    return 0;
}
