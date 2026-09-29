// Slide reference: SLIDE 14 - Incrementing an Array in Parallel (also LAB 3 - Array Increment)
// Module 2: increment every element of an array in parallel.
// Each thread handles a different range of indices - no synchronization
// is needed because each array element is touched by exactly one thread.

#include <cstdio>
#include <chrono>
#include <omp.h>

int main() {
    const int N = 2000000;
    int arr[N];
    for (int i = 0; i < N; i++) arr[i] = i;

    auto start = std::chrono::high_resolution_clock::now();

    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        arr[i] = arr[i] + 1;
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;

    for (int i = 0; i < 10; i++) printf("%d ", arr[i]);
    printf("\n");
    printf("Time (OpenMP, %d threads): %f seconds\n",
           omp_get_max_threads(), elapsed.count());

    return 0;
}
