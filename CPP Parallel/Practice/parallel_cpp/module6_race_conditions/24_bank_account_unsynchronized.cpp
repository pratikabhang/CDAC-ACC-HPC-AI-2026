// Slide reference: SLIDE 16 - Race Conditions (also LAB 4 - Race Condition
// Demonstration)
// Module 6: a second race condition example, on a more relatable shared
// resource than a bare counter. Two threads deposit into the same bank
// account balance with no protection - "balance = balance + 1" is still
// just a read-modify-write, so deposits can be lost exactly like
// counter++ was lost in 21_counter_unsynchronized.cpp.
// Run this multiple times - the result will often be less than expected.

#include <cstdio>
#include <thread>

long balance = 1000;   // starting balance

const int ITERATIONS = 5000000;

void deposit() {
    for (int i = 0; i < ITERATIONS; i++) {
        balance = balance + 1;   // NOT thread-safe
    }
}

int main() {
    std::thread t1(deposit);
    std::thread t2(deposit);

    t1.join();
    t2.join();

    printf("Balance (unsynchronized): %ld  (expected %ld)\n",
           balance, 1000 + 2L * ITERATIONS);
    return 0;
}
