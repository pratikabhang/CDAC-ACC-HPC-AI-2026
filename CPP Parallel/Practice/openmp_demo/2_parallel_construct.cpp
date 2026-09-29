#include <iostream>
#include <omp.h>

int main() {
    omp_set_num_threads(4);    // sets the number of threads to be used in parallel region

#pragma omp parallel
    {
        int ID = omp_get_thread_num();    // returns the unique thread ID of the calling thread within a parallel region
        std::cout << "Hello my ID is :" << ID << std::endl;
    }
    return 0;
}
