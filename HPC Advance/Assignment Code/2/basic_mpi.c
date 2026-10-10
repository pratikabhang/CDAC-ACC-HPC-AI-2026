#include <mpi.h>
#include <stdio.h>
#include <string.h>

#define MAX_MSG_LEN 100

int main(int argc, char *argv[]) {
    int rank, size;
    char message[MAX_MSG_LEN];
    int i;

    // Initialize the MPI environment
    MPI_Init(&argc, &argv);

    // Get the number of processes
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    // Get the rank of the process
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    if (rank == 0) {
        // Root process sends a message to all other processes
        strcpy(message, "Hello from root process!");
        for (i = 1; i < size; ++i) {
            MPI_Send(message, strlen(message) + 1, MPI_CHAR, i, 0, MPI_COMM_WORLD);
        }
    } else {
        // Other processes receive the message
        MPI_Recv(message, MAX_MSG_LEN, MPI_CHAR, 0, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
        printf("Process %d received message: %s\n", rank, message);
    }

    // Finalize the MPI environment
    MPI_Finalize();
    return 0;
}

