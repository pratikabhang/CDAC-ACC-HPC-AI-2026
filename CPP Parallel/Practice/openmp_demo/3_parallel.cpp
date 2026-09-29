#include <iostream>
#include <omp.h>
// number of threads in a parallel region : precedence in ascending order
// 1. number of CPU cores on node
// 2. environment variable cmd> export OMP_NUM_THREADS=12

int main()
{
    omp_set_num_threads(8);    // 3.
    //#pragma omp parallel                          //equivalent to: #pragma omp parallel if(1)
    //#pragma omp parallel num_threads(4)            //4.
    //#pragma omp parallel num_threads(4) if(0)      //5.
    #pragma omp parallel num_threads(4) if(1)
    {
        std::cout << "parallel region" << std::endl;
    }

    std::cout << "serial region" << std::endl;

    return 0;
}
