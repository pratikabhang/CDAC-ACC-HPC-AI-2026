#include <iostream>
#include <vector>
#include <omp.h>

int main() {
    const int N = 6;
    std::vector<int> A = {10, 20, 30, 40, 50, 60};
    std::vector<int> B = {1, 2, 3, 4, 5, 6};
    std::vector<int> C(N, 0);

    // Set thread count to 3
    omp_set_num_threads(3);

    #pragma omp parallel for
    for (int i = 0; i < N; ++i) {
        C[i] = A[i] + B[i];

        // Ensure console output is non-garbled
        #pragma omp critical
        {
            std::cout << "Thread " << omp_get_thread_num() 
                      << " computed index " << i 
                      << ": " << A[i] << " + " << B[i] << " = " << C[i] << "\n";
        }
    }

    std::cout << "\nFinal Output Array: ";
    for (int val : C) {
        std::cout << val << " ";
    }
    std::cout << "\n";

    return 0;
}

