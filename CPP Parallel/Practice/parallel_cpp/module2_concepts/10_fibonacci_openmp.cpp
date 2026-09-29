// Slide reference: SLIDE 13 - Parallel Fibonacci (also LAB 2 - Parallel Fibonacci)
// Module 2: parallel Fibonacci using OpenMP tasks.
// Same recursive structure as fibonacci_serial.cpp, with tasks added.
// A threshold avoids creating tasks for very small subproblems.

#include <cstdio>
#include <chrono>
#include <omp.h>

const int THRESHOLD = 20;

long fib(int n) {
    if (n < 2) return n;

    if (n <= THRESHOLD) {
        // Below the threshold, run sequentially - too small to be worth a task.
        return fib(n - 1) + fib(n - 2);
    }

    long a, b;

    #pragma omp task shared(a)
    a = fib(n - 1);

    #pragma omp task shared(b)
    b = fib(n - 2);

    #pragma omp taskwait
    return a + b;
}

int main() {
    int n = 50;
    long result;

    auto start = std::chrono::high_resolution_clock::now();

    #pragma omp parallel
    {
        #pragma omp single
        result = fib(n);
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;

    printf("fib(%d) = %ld\n", n, result);
    printf("Time (OpenMP, %d threads): %f seconds\n",
           omp_get_max_threads(), elapsed.count());

    return 0;
}
