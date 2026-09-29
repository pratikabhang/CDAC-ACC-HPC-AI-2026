#include <iostream>
#include <vector>
#include <omp.h>

int main() {
    const size_t size = 2'000'000;
    std::vector<int> arr(size);

    // Initialize arr[i] = (i % 100) - 50
    for (size_t i = 0; i < size; ++i) {
        arr[i] = (i % 100) - 50;
    }

    // 1. Without Synchronization (Data Race)
    int pos_no_sync = 0, neg_no_sync = 0;
    #pragma omp parallel for
    for (size_t i = 0; i < size; ++i) {
        if (arr[i] > 0) pos_no_sync++;
        else if (arr[i] < 0) neg_no_sync++;
    }

    // 2. With Synchronization (Using reduction)
    int pos_sync = 0, neg_sync = 0;
    #pragma omp parallel for reduction(+:pos_sync, neg_sync)
    for (size_t i = 0; i < size; ++i) {
        if (arr[i] > 0) pos_sync++;
        else if (arr[i] < 0) neg_sync++;
    }

    std::cout << "--- Problem 2: Count Positive & Negative ---\n";
    std::cout << "Without Synchronization:\n";
    std::cout << "  Positive count: " << pos_no_sync << "\n";
    std::cout << "  Negative count: " << neg_no_sync << "\n";
    std::cout << "With Synchronization (reduction):\n";
    std::cout << "  Positive count: " << pos_sync << "\n";
    std::cout << "  Negative count: " << neg_sync << "\n\n";

    return 0;
}
