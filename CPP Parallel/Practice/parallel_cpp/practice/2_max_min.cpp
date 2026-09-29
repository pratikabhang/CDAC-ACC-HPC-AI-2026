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
    int min_total = 0;
    int max_total = 0;

    MPI_Reduce(&local_total, &grand_total, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);

    MPI_Reduce(&local_total, &min_total, 1, MPI_INT, MPI_MIN, 0, MPI_COMM_WORLD);

    MPI_Reduce(&local_total, &max_total, 1, MPI_INT, MPI_MAX, 0, MPI_COMM_WORLD);

    if (rank == 0) {
        cout << "\n--- Master Rank 0 Results ---" << endl;
        cout << "Grand Total: " << grand_total << endl;
        cout << "Minimum Local Total: " << min_total << endl;
        cout << "Maximum Local Total: " << max_total << endl;
        cout << "-----------------------------" << endl;
    }

    MPI_Finalize();
    return 0;
}
