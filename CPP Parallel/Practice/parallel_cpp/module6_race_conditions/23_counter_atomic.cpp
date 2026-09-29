// Slide reference: SLIDE 47 - Atomic Operations (also LAB 4 - Race Condition Demonstration)
// Module 6: race condition fixed with std::atomic.
// counter++ on a std::atomic<int> is a single indivisible operation,
// giving a correct result, usually with less overhead than a mutex
// for a simple case like this.

#include <cstdio>
#include <thread>
#include <atomic>

std::atomic<int> counter(0);

const int ITERATIONS = 5000000;

void increment() {
    for (int i = 0; i < ITERATIONS; i++) {
        counter++;
    }
}

int main() {
    std::thread t1(increment);
    std::thread t2(increment);

    t1.join();
    t2.join();

    printf("Counter (atomic): %d  (expected %d)\n", counter.load(), 2 * ITERATIONS);
    return 0;
}
