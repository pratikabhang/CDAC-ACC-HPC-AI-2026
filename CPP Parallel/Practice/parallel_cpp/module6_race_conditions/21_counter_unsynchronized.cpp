// Slide reference: SLIDE 16 - Race Conditions, SLIDE 44 - Race Conditions and Concurrency (also LAB 4 - Race Condition Demonstration)
// Module 6: race condition demonstration (BUGGY - on purpose).
// Two threads increment the same variable with no protection.
// counter++ is really read-modify-write, so updates can be lost.
// Run this multiple times - the result will often NOT be 2000.

#include <cstdio>
#include <thread>

int counter = 0;

const int ITERATIONS = 5000000;

void increment() {
    for (int i = 0; i < ITERATIONS; i++) {
        counter++;   // NOT thread-safe
    }
}

int main() {
    std::thread t1(increment);
    std::thread t2(increment);

    t1.join();
    t2.join();

    printf("Counter (unsynchronized): %d  (expected %d)\n",
           counter, 2 * ITERATIONS);
    return 0;
}
