#include <iostream>
#include <mpi.h>

using namespace std;

int main(int argc, char* argv[]) {
    MPI_Init(&argc, &argv);
    
    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int deposits[2];

    if (rank == 0) {
        deposits[0] = 10000;
        deposits[1] = 20000;
    }
    else if (rank == 1) {
        deposits[0] = 15000;
        deposits[1] = 25000;
    }
    else if (rank == 2) {
        deposits[0] = 20000;
        deposits[1] = 30000;
    }
    else if (rank == 3) {
        deposits[0] = 25000;
        deposits[1] = 35000;
    }
    else {
        deposits[0] = 0;
        deposits[1] = 0;
    }

    int local_total = deposits[0] + deposits[1];
    
    cout << "Rank " << rank << " local total: " << local_total << endl;

    int grand_total = 0;

    MPI_Reduce(
        &local_total,     // Send buffer: address of local data
        &grand_total,     // Receive buffer: address to store the result
        1,                // Count: number of elements being reduced
        MPI_INT,          // Datatype of elements
        MPI_SUM,          // Operation: add all values together
        0,                // Root rank: the process that receives the grand total
        MPI_COMM_WORLD    // Communicator
    );

    if (rank == 0) {
        cout << "--- Grand Total across all ranks: " << grand_total << " ---" << endl;
    }

    MPI_Finalize();
    return 0;
}
