#include <iostream>
#include <omp.h>

int main() {

    omp_set_num_threads(4);

     #pragma omp parallel        //2. usage of 'for' clause
     {
        //#pragma omp parallel for    //1. usage of 'for' clause
        #pragma omp for
        for (int i = 0; i < 10; i++) {
            std::cout << "Thread " << omp_get_thread_num() << " is processing iteration " << i << std::endl;
       }
     }

    return 0;
}
