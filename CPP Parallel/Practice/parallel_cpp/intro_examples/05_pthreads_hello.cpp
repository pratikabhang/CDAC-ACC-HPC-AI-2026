// Slide reference: SLIDE 11 - Pthreads and OpenMP
// Introductory example: Pthreads basics
// pthread_create starts a new thread; pthread_join waits for it to finish.
#include <iostream>
#include <pthread.h>

void* worker(void* arg)
{
    int value = *(int*)arg;

    std::cout << "Value = "
              << value << "\n";

    return NULL;
}

int main()
{
    pthread_t threads[5];

    int values[5] = {100, 200, 300, 400, 500};

    // Create 5 threads
    for (int i = 0; i < 5; i++)
    {
        pthread_create(
            &threads[i],
            NULL,
            worker,
            &values[i]
        );
    }

    // Wait for all 5 threads
    for (int i = 0; i < 5; i++)
    {
        pthread_join(threads[i], NULL);
    }

    return 0;
}