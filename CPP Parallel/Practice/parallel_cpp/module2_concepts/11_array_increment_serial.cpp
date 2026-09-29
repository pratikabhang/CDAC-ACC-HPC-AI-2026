// Slide reference: SLIDE 14 - Incrementing an Array in Parallel (also LAB 3 - Array Increment)
// Module 2: increment every element of an array sequentially.

#include <cstdio>
#include <chrono>

int main() {
    const int N = 2000000;
    int arr[N];
    for (int i = 0; i < N; i++) arr[i] = i;

    auto start = std::chrono::high_resolution_clock::now();

    for (int i = 0; i < N; i++) {
        arr[i] = arr[i] + 1;
    }

    auto end = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = end - start;

    for (int i = 0; i < 10; i++) printf("%d ", arr[i]);
    printf("\n");
    printf("Time (serial): %f seconds\n", elapsed.count());

    return 0;
}
