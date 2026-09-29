#include <iostream>
#include <mpi.h>
#include <cmath> 

using namespace std;

int main(int argc, char* argv[]) {
    MPI_Init(&argc, &argv);

    int rank, size;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &size);

    int deposits[2];

    // Assign data based on rank (Hardcoded for up to 4 ranks)
    if (rank == 0) {
        deposits[0] = 10000;
        deposits[1] = 20000;
    } else if (rank == 1) {
        deposits[0] = 15000;
        deposits[1] = 25000;
    } else if (rank == 2) {
        deposits[0] = 20000;
        deposits[1] = 30000;
    } else if (rank == 3) {
        deposits[0] = 25000;
        deposits[1] = 35000;
    } else {
        deposits[0] = 0;
        deposits[1] = 0;
    }

    int local_total = deposits[0] + deposits[1];

    // 1. Allreduce sums up totals and gives the grand total to ALL ranks instantly
    int grand_total = 0;
    MPI_Allreduce(&local_total, &grand_total, 1, MPI_INT, MPI_SUM, MPI_COMM_WORLD);

    // 2. Compute and print the flat contribution percentage for each rank
    float local_percentage = 0.0f;
    if (grand_total > 0) {
        local_percentage = (static_cast<float>(local_total) / grand_total) * 100.0f;
    }
    
    cout << "Rank " << rank << " local total: " << local_total 
         << " (" << local_percentage << "%)" << endl;

    // 3. Compute global average
    double average = static_cast<double>(grand_total) / size;

    if (rank == 0) {
        cout << "\n--- Master Rank 0 Results ---" << endl;
        cout << "Grand Total: " << grand_total << endl;
        cout << "Average: " << average << endl;
    }

    // 4. Calculate local absolute deviation from global average
    double local_deviation = abs(local_total - average);

    // 5. Sum all the deviations back onto Rank 0
    double grand_deviation_total = 0.0;
    MPI_Reduce(&local_deviation, &grand_deviation_total, 1, MPI_DOUBLE, MPI_SUM, 0, MPI_COMM_WORLD);

    // 6. Final calculation and print on Rank 0
    if (rank == 0) {
        double average_deviation = grand_deviation_total / size;
        cout << "Average Deviation: " << average_deviation << endl;
        cout << "-----------------------------" << endl;
    }

    MPI_Finalize();
    return 0;
}
