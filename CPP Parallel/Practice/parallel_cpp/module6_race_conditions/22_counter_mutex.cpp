// Slide reference: SLIDE 45 - Eliminating Race Conditions by Synchronization (also LAB 4 - Race Condition Demonstration)
// Module 6: race condition fixed with a mutex.
// Only one thread at a time can hold the lock and update counter,
// so the result is always correct - but locking has some overhead.

#include <cstdio>
#include <thread>
#include <mutex>

int counter = 0;
std::mutex counterMutex;

const int ITERATIONS = 5000000;

void increment() {
    for (int i = 0; i < ITERATIONS; i++) {
        std::lock_guard<std::mutex> lock(counterMutex);
        counter++;
    }
}

int main() {
    std::thread t1(increment);
    std::thread t2(increment);

    t1.join();
    t2.join();

    printf("Counter (mutex): %d  (expected %d)\n", counter, 2 * ITERATIONS);
    return 0;
}
