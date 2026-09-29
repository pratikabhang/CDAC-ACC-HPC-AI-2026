// Slide reference: SLIDE 14 - Incrementing an Array in Parallel (also LAB 3 - Array Increment)
// Module 2: compute-heavy version of the array increment demo, in parallel.
// Same per-element work as 11b_array_sqrt_serial.cpp (repeated sqrt), so the
// loop is compute-bound rather than memory-bound. With enough work per
// element, the OpenMP fork/join overhead is dwarfed by the compute saved,
// and this version should actually be faster than the serial one.

#include <cstdio>
#include <chrono>
#include <cmath>
#include <omp.h>
#include <vector>

int main() {
    const int N = 2000000;
    std::vector<double> arr(N);
    for (int i = 0; i < N; i++) arr[i] = i;

    auto start = std::chrono::high_resolution_clock::now();

    #pragma omp parallel for
    for (int i = 0; i < N; i++) {
        double val = arr[i];
        for (int j = 0; j < 100; j++) val = std::sqrt(val + 1.0);
        arr[i] = val;
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;

    for (int i = 0; i < 10; i++) printf("%f ", arr[i]);
    printf("\n");
    printf("Time (OpenMP, %d threads, sqrt): %f seconds\n",
           omp_get_max_threads(), elapsed.count());

    return 0;
}
