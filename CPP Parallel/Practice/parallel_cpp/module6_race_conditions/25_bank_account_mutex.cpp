// Slide reference: SLIDE 45 - Eliminating Race Conditions by Synchronization
// Module 6: the bank account race fixed with a mutex - the same fix as
// 22_counter_mutex.cpp, applied to 24_bank_account_unsynchronized.cpp.
// Only one thread at a time can hold the lock and update balance, so the
// result is always correct - but locking has some overhead. Compare with
// 26_bank_account_ownership.cpp, which fixes the same race a different
// way: no lock at all, by redesigning who owns the data.

#include <cstdio>
#include <thread>
#include <mutex>

long balance = 1000;
std::mutex balanceMutex;

const int ITERATIONS = 5000000;

void deposit() {
    for (int i = 0; i < ITERATIONS; i++) {
        std::lock_guard<std::mutex> lock(balanceMutex);
        balance = balance + 1;
    }
}

int main() {
    std::thread t1(deposit);
    std::thread t2(deposit);

    t1.join();
    t2.join();

    printf("Balance (mutex): %ld  (expected %ld)\n",
           balance, 1000 + 2L * ITERATIONS);
    return 0;
}
