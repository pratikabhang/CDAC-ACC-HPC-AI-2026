#include <iostream>
#include <vector>
#include <algorithm>
#include <execution>
#include <chrono>

int main() {
    const int fixed_val = 10;
    std::vector<int> vec_seq(1'000'000, 5);
    std::vector<int> vec_par = vec_seq;

    auto add_val = [fixed_val](int &n) {
        n += fixed_val;
    };

    // Sequential Execution
    auto start_seq = std::chrono::high_resolution_clock::now();
    std::for_each(std::execution::seq, vec_seq.begin(), vec_seq.end(), add_val);
    auto end_seq = std::chrono::high_resolution_clock::now();

    // Parallel Execution
    auto start_par = std::chrono::high_resolution_clock::now();
    std::for_each(std::execution::par, vec_par.begin(), vec_par.end(), add_val);
    auto end_par = std::chrono::high_resolution_clock::now();

    std::chrono::duration<double, std::milli> duration_seq = end_seq - start_seq;
    std::chrono::duration<double, std::milli> duration_par = end_par - start_par;

    std::cout << "Sequential addition time: " << duration_seq.count() << " ms\n";
    std::cout << "Parallel addition time:   " << duration_par.count() << " ms\n";

    return 0;
}
