#include <iostream>
#include <omp.h>

#define SIZE 1024

void matrix_multiply(int A[][SIZE], int B[][SIZE], int C[][SIZE]) {
    #pragma omp parallel for //note: this will be create parallel region for matrix multiplication, comment and uncomment this line and observe the time taken in computation
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            C[i][j] = 0;
            for (int k = 0; k < SIZE; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

int main() {
    static int A[SIZE][SIZE];
    static int B[SIZE][SIZE];
    static int C[SIZE][SIZE];

    // Initialize matrices A and B
    for (int i = 0; i < SIZE; i++) {
        for (int j = 0; j < SIZE; j++) {
            A[i][j] = i + j;
            B[i][j] = i - j;
        }
    }

    double start_time = omp_get_wtime();    // returns the elapsed wall-clock time in seconds

    // Perform matrix multiplication
    matrix_multiply(A, B, C);

    double end_time = omp_get_wtime();
    std::cout << "Execution time: " << (end_time - start_time) << " seconds" << std::endl;

    return 0;
}
