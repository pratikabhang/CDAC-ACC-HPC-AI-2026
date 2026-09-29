#include <iostream>
#include <vector>
#include <algorithm>
#include <omp.h>

int main() {
    const size_t size = 1'000'000;
    std::vector<int> arr(size);

    // Initialize arr[i] = i % 10000
    for (size_t i = 0; i < size; ++i) {
        arr[i] = static_cast<int>(i % 10000);
    }

    // 1. Without Synchronization (Data Race)
    int max_no_sync = -1;
    #pragma omp parallel for
    for (size_t i = 0; i < size; ++i) {
        if (arr[i] > max_no_sync) {
            max_no_sync = arr[i]; // Unsynchronized read & write
        }
    }

    // 2. With Synchronization (Using OpenMP reduction max clause)
    int max_sync = -1;
    #pragma omp parallel for reduction(max:max_sync)
    for (size_t i = 0; i < size; ++i) {
        if (arr[i] > max_sync) {
            max_sync = arr[i];
        }
    }

    std::cout << "--- Problem 3: Maximum Value ---\n";
    std::cout << "Max Without Sync (Unreliable): " << max_no_sync << "\n";
    std::cout << "Max With Sync (reduction max): " << max_sync << "\n";

    return 0;
}