#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
#include<omp.h>
#define WORK_SIZE 10000     // Amount of work per loop
#define REPEAT 100000       // Repeat to increase run time

// Simulate computational work
double do_heavy_work(int rank) {
    double result = 0.0;
    double *arr = malloc(WORK_SIZE * sizeof(double));

    for (int i = 0; i < WORK_SIZE; ++i)
        arr[i] = i * 0.00001;

    for (int r = 0; r < REPEAT; ++r) {
#pragma omp simd reduction(+:result)
        for (int i = 0; i < WORK_SIZE; ++i) {
            result += arr[i] * arr[i] + arr[i];
        }
    }

    free(arr);
    return result + rank;
}

int main(int argc, char *argv[]) {
    int rank, size;
    double local_result, global_result;
    double start_time, end_time;

    MPI_Init(&argc, &argv);                 // Initialize MPI
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);   // Get this process's rank
    MPI_Comm_size(MPI_COMM_WORLD, &size);   // Get number of processes

    if (rank == 0) {
        printf("Starting long-running unoptimized MPI computation with %d processes...\n", size);
    }

    start_time = MPI_Wtime();               // Start timing

    // Perform dummy workload
    local_result = do_heavy_work(rank);

    // Aggregate results (blocking and serial)
    MPI_Reduce(&local_result, &global_result, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    end_time = MPI_Wtime();                 // End timing

    if (rank == 0) {
        printf("Global result: %f\n", global_result);
        printf("Total time: %f seconds\n", end_time - start_time);
    }

    MPI_Finalize();                         // Finalize MPI
    return 0;
}

