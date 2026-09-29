// Slide reference: SLIDE 11 - Pthreads and OpenMP
// Module 2: sum an array using Pthreads.
// Each thread sums its own chunk into a separate slot; no shared-write races.
// Compare the syntax and effort here with 14b_sum_openmp_reduction.cpp -
// both avoid the shared-write race, just with very different amounts of code.

#include <cstdio>
#include <pthread.h>

const int N = 20;
const int NUM_THREADS = 4;

int arr[N];
long partialSums[NUM_THREADS];

struct ThreadArgs {
    int start;
    int end;
    int threadId;
};

void* sumRange(void* argPtr) {
    ThreadArgs* args = (ThreadArgs*)argPtr;
    long sum = 0;
    for (int i = args->start; i < args->end; i++) {
        sum += arr[i];
    }
    partialSums[args->threadId] = sum;
    return nullptr;
}

int main() {
    for (int i = 0; i < N; i++) arr[i] = i + 1;   // 1..20

    pthread_t threads[NUM_THREADS];
    ThreadArgs args[NUM_THREADS];
    int chunk = N / NUM_THREADS;

    for (int t = 0; t < NUM_THREADS; t++) {
        args[t].start = t * chunk;
        args[t].end = (t == NUM_THREADS - 1) ? N : (t + 1) * chunk;
        args[t].threadId = t;
        pthread_create(&threads[t], nullptr, sumRange, &args[t]);
    }

    for (int t = 0; t < NUM_THREADS; t++) {
        pthread_join(threads[t], nullptr);
    }

    long total = 0;
    for (int t = 0; t < NUM_THREADS; t++) total += partialSums[t];

    printf("Total sum (Pthreads): %ld\n", total);   // 210
    return 0;
}
