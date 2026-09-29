#include <iostream>
#include <vector>
#include <numeric>
#include <chrono>
#include <omp.h>

int main() {
    const size_t size = 1'000'000;
    std::vector<long long> arr(size);

    // Initialize arr[i] = i
    for (size_t i = 0; i < size; ++i) {
        arr[i] = i;
    }

    // 1. Without Synchronization (Data Race Expected)
    long long total_without_sync = 0;
    #pragma omp parallel for
    for (size_t i = 0; i < size; ++i) {
        total_without_sync += arr[i]; // Concurrent writes cause race condition
    }

    // 2. With Synchronization (Using reduction)
    long long total_with_sync = 0;
    #pragma omp parallel for reduction(+:total_with_sync)
    for (size_t i = 0; i < size; ++i) {
        total_with_sync += arr[i];
    }

    // Expected mathematical total: n * (n - 1) / 2
    long long expected_total = (static_cast<long long>(size) * (size - 1)) / 2;

    std::cout << "--- Problem 1: Array Sum ---\n";
    std::cout << "Expected Total:             " << expected_total << "\n";
    std::cout << "Without Sync (Race Condition): " << total_without_sync << "\n";
    std::cout << "With Sync (#pragma reduction): " << total_with_sync << "\n\n";

    return 0;
}
