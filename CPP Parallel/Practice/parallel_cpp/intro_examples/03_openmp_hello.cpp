// Slide reference: SLIDE 11 - Pthreads and OpenMP
// Introductory example: OpenMP basics
// #pragma omp parallel starts a team of threads that all run the block below.

#include <cstdio>
#include <omp.h>

int main() {
    #pragma omp parallel
    {
        int id = omp_get_thread_num();
        int total = omp_get_num_threads();
        printf("Hello from thread %d of %d\n", id, total);
    }
    return 0;
}
