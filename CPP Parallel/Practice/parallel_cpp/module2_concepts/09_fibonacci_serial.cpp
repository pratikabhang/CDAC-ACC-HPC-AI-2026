// Slide reference: SLIDE 13 - Parallel Fibonacci (also LAB 1 - Sequential Baseline)
// Module 2: sequential Fibonacci - baseline for later comparison.

#include <cstdio>
#include <chrono>

long fib(int n) {
    if (n < 2) return n;
    return fib(n - 1) + fib(n - 2);
}

int main() {
    int n = 50;

    auto start = std::chrono::high_resolution_clock::now();
    long result = fib(n);
    auto end = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double> elapsed = end - start;

    printf("fib(%d) = %ld\n", n, result);
    printf("Time (serial): %f seconds\n", elapsed.count());

    return 0;
}
