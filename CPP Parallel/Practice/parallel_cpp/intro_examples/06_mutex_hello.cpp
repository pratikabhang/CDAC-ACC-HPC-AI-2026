// Slide reference: SLIDE 45 - Eliminating Race Conditions by Synchronization
// Introductory example: mutex basics
// A mutex lets only one thread at a time execute the protected code,
// so the shared counter is always updated safely.

#include <cstdio>
#include <thread>
#include <mutex>

int counter = 0;
std::mutex counterMutex;

void increment() {
    for (int i = 0; i < 1000; i++) {
        std::lock_guard<std::mutex> lock(counterMutex);
        counter++;
    }
}

int main() {
    std::thread t1(increment);
    std::thread t2(increment);

    t1.join();
    t2.join();

    printf("Counter: %d\n", counter);   // always 2000
    return 0;
}
