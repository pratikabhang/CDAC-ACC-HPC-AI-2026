// Same code using openmp
#include <iostream>
#include <omp.h>

int main()
{
    int values[5] = {100, 200, 300, 400, 500};

    // Automatically create threads and distribute the 5 loop iterations
    #pragma omp parallel for num_threads(5)
    for (int i = 0; i < 5; i++)
    {
        int value = values[i];

        #pragma omp critical
        {
            std::cout << "Value = " << value 
                      << " (Processed by thread " << omp_get_thread_num() << ")\n";
        }
    }

    return 0;
}
