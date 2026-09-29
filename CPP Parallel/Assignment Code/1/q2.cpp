#include <iostream>
#include <vector>
#include <algorithm>
#include <execution>

int main() {
    std::vector<int> vec = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12};

    // Lambda to calculate the cube
    auto cube = [](int &n) {
        n = n * n * n;
    };

    // Execute sequentially
    std::for_each(std::execution::seq, vec.begin(), vec.end(), cube);

    std::cout << "First 10 cubed results: ";
    for (int i = 0; i < 10; ++i) {
        std::cout << vec[i] << " ";
    }
    std::cout << "\n";

    return 0;
}
