// Slide reference: SLIDE 16 - Race Conditions ("...correct synchronization
// OR redesigned data ownership is required")
// Module 6: the bank account race fixed WITHOUT any synchronization, by
// redesigning who owns the data instead. Compare with
// 25_bank_account_mutex.cpp, which fixes the same race by locking access
// to a variable both threads still share.
//
// Here, each thread only ever touches its OWN private running total -
// there is no shared variable during the parallel work at all, so there
// is nothing to race on. Only after both threads finish does a single
// thread (main) combine the two private totals into the account balance -
// one combine step, done by one thread, needs no lock.

#include <cstdio>
#include <thread>

const int ITERATIONS = 5000000;
long threadTotal[2] = {0, 0};   // each thread owns exactly one slot

void deposit(int id) {
    long total = 0;   // private to this thread
    for (int i = 0; i < ITERATIONS; i++) {
        total = total + 1;
    }
    threadTotal[id] = total;   // one write, from the thread that owns it
}

int main() {
    long balance = 1000;

    std::thread t1(deposit, 0);
    std::thread t2(deposit, 1);

    t1.join();
    t2.join();

    balance += threadTotal[0] + threadTotal[1];   // combined by one thread, once

    printf("Balance (redesigned ownership): %ld  (expected %ld)\n",
           balance, 1000 + 2L * ITERATIONS);
    return 0;
}
