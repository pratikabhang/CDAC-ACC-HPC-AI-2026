// Slide reference: SLIDE 38 - Reduction (also LAB 5 - Reduction)
// Module 5: reduction.
// Each thread computes a local sum; OpenMP combines the local sums
// into one final result using the reduction clause.

#include <cstdio>

int main() {
    const int N = 16;
    int arr[N];
    for (int i = 0; i < N; i++) arr[i] = i + 1;   // 1..16

    long total = 0;

    #pragma omp parallel for reduction(+:total)
    for (int i = 0; i < N; i++) {
        total += arr[i];
    }

    printf("Sum via reduction: %ld\n", total);   // 136
    return 0;
}
