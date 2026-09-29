#include <iostream>
#include <vector>
#include <algorithm>
#include <execution>
#include <chrono>

int main() {
    // Vector of 1,000,000 elements initialized to 4
    std::vector<int> vec(1'000'000, 4);

    auto start = std::chrono::high_resolution_clock::now();

    // Square each element exactly once in-place
    std::for_each(std::execution::seq, vec.begin(), vec.end(), [](int &n) {
        n = n * n;
    });

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> duration = end - start;

    std::cout << "First 10 elements: ";
    for (int i = 0; i < 10; ++i) {
        std::cout << vec[i] << " ";
    }
    std::cout << "\nExecution time (seq): " << duration.count() << " ms\n";

    return 0;
}
