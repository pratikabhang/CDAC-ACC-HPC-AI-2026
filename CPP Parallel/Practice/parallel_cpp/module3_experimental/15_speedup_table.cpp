// Slide reference: SLIDE 8 - Speedup, SLIDE 9 - Efficiency (also LAB 7 - Speedup and Efficiency)
// Module 3: measure speedup and efficiency across different thread counts.
// Runs the same parallel Fibonacci computation with 1, 2, 4, and 8 threads
// and prints a small table - no plotting library needed.

#include <cstdio>
#include <chrono>
#include <omp.h>

const int THRESHOLD = 20;

long fib(int n) {
    if (n < 2) return n;

    if (n <= THRESHOLD) {
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

double timeFibWithThreads(int n, int numThreads) {
    omp_set_num_threads(numThreads);
    long result;

    auto start = std::chrono::high_resolution_clock::now();

    #pragma omp parallel
    {
        #pragma omp single
        result = fib(n);
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;

    (void)result;
    return elapsed.count();
}

int main() {
    int n = 30;
    int threadCounts[] = {1, 2, 4, 8};

    double baseline = timeFibWithThreads(n, 1);

    printf("%-10s %-15s %-10s %-10s\n", "Threads", "Time (s)", "Speedup", "Efficiency");

    for (int t : threadCounts) {
        double time = timeFibWithThreads(n, t);
        double speedup = baseline / time;
        double efficiency = speedup / t;
        printf("%-10d %-15f %-10f %-10f\n", t, time, speedup, efficiency);
    }

    return 0;
}
