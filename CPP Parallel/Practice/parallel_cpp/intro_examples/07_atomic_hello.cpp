// Slide reference: SLIDE 47 - Atomic Operations
// Introductory example: atomic operations
// std::atomic<int> makes counter++ a single indivisible operation,
// so no lock is needed for this simple case.

#include <cstdio>
#include <thread>
#include <atomic>

std::atomic<int> counter(0);

void increment() {
    for (int i = 0; i < 1000; i++) {
        counter++;
    }
}

int main() {
    std::thread t1(increment);
    std::thread t2(increment);

    t1.join();
    t2.join();

    printf("Counter: %d\n", counter.load());   // always 2000
    return 0;
}
