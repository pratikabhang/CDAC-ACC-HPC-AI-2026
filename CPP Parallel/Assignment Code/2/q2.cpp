#include <iostream>
#include <vector>
#include <omp.h>

int main() {
    std::vector<int> arr = {5, 12, 8, 20, 15, 3, 9, 11}; // Array of 8 integers
    int total_sum = 0;

    // Use OpenMP reduction clause with 4 threads
    #pragma omp parallel for num_threads(4) reduction(+:total_sum)
    for (size_t i = 0; i < arr.size(); ++i) {
        total_sum += arr[i];
    }

    std::cout << "Final Total Sum: " << total_sum << "\n";

    return 0;
}

