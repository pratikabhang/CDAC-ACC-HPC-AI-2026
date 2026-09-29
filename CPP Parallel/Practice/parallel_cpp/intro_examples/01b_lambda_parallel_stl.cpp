// Slide reference: SLIDE 4 - Lambda Expressions
// Introductory example: the same lambda syntax from 01_lambda_hello.cpp,
// now passed to a C++17 standard-library algorithm instead of OpenMP or
// Pthreads. std::execution::par is a hint to the library that the
// algorithm may run its work across multiple threads - no #pragma, no
// manual thread management, just a lambda and an execution policy.
//
// Requires linking against Intel TBB (-ltbb), which is what GCC's
// libstdc++ uses to actually run std::execution::par in parallel. Without
// it, the code still compiles and runs correctly, but silently falls back
// to sequential execution.

#include <cstdio>
#include <chrono>
#include <cmath>
#include <vector>
#include <algorithm>
#include <execution>

int main() {
    const int N = 2000000;
    std::vector<double> v(N);
    for (int i = 0; i < N; i++) v[i] = i;

    // Squaring each element, repeated with a modulo to keep values bounded
    // and add enough work per element to make the loop compute-bound
    // rather than memory-bound (see 11b_array_sqrt_serial.cpp for the
    // same idea applied to sqrt).
    auto square = [](double& x) {
        for (int j = 0; j < 50; j++) x = std::fmod(x * x + 1.0, 1000000.0);
    };

    auto start = std::chrono::high_resolution_clock::now();
    std::for_each(std::execution::seq, v.begin(), v.end(), square);
    auto mid = std::chrono::high_resolution_clock::now();

    for (int i = 0; i < N; i++) v[i] = i;

    std::for_each(std::execution::par, v.begin(), v.end(), square);
    auto end = std::chrono::high_resolution_clock::now();

    for (int i = 0; i < 10; i++) printf("%f ", v[i]);
    printf("\n");

    std::chrono::duration<double> seq_time = mid - start;
    std::chrono::duration<double> par_time = end - mid;
    printf("Time (seq): %f seconds\n", seq_time.count());
    printf("Time (par): %f seconds\n", par_time.count());

    return 0;
}
