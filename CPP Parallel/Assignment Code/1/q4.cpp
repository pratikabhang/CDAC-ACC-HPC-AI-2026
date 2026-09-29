#include <iostream>
#include <vector>
#include <algorithm>
#include <execution>
#include <chrono>
#include <cmath>
#include <numeric>

int main() {
    std::vector<double> vec_seq(1'000'000);
    // Fill vector with values 1 to 1,000,000
    std::iota(vec_seq.begin(), vec_seq.end(), 1.0);
    std::vector<double> vec_par = vec_seq;

    auto math_op = [](double &x) {
        x = std::sqrt(x) + 1.0;
    };

    // Sequential Execution
    auto start_seq = std::chrono::high_resolution_clock::now();
    std::for_each(std::execution::seq, vec_seq.begin(), vec_seq.end(), math_op);
    auto end_seq = std::chrono::high_resolution_clock::now();

    // Parallel Execution
    auto start_par = std::chrono::high_resolution_clock::now();
    std::for_each(std::execution::par, vec_par.begin(), vec_par.end(), math_op);
    auto end_par = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double, std::milli> duration_seq = end_seq - start_seq;
    std::chrono::duration<double, std::milli> duration_par = end_par - start_par;

    std::cout << "Sequential execution time: " << duration_seq.count() << " ms\n";
    std::cout << "Parallel execution time:   " << duration_par.count() << " ms\n";

    return 0;
}

