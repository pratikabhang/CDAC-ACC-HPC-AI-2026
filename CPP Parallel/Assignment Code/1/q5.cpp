#include <iostream>
#include <vector>
#include <algorithm>
#include <execution>
#include <chrono>

int main() {
    int factor = 5;
    std::vector<int> vec_seq = {5, 10, 15, 20};
    std::vector<int> vec_par = vec_seq;

    // Capture 'factor' by value
    auto multiply = [factor](int &n) {
        n *= factor;
    };

    // Sequential Execution
    auto start_seq = std::chrono::high_resolution_clock::now();
    std::for_each(std::execution::seq, vec_seq.begin(), vec_seq.end(), multiply);
    auto end_seq = std::chrono::high_resolution_clock::now();

    // Parallel Execution
    auto start_par = std::chrono::high_resolution_clock::now();
    std::for_each(std::execution::par, vec_par.begin(), vec_par.end(), multiply);
    auto end_par = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double, std::milli> duration_seq = end_seq - start_seq;
    std::chrono::duration<double, std::milli> duration_par = end_par - start_par;

    std::cout << "Result vector: ";
    for (int val : vec_seq) {
        std::cout << val << " ";
    }
    std::cout << "\n";

    std::cout << "Sequential execution time: " << duration_seq.count() << " ms\n";
    std::cout << "Parallel execution time:   " << duration_par.count() << " ms\n";

    return 0;
}
