#include <stdio.h>
#include <cuda_runtime.h>

__global__ void hello() {
    printf("Hello from GPU thread %d!\n", threadIdx.x);
}

int main() {
    hello<<<1, 5>>>();
    cudaError_t err = cudaGetLastError();
    if (err != cudaSuccess) {
        printf("Kernel launch error: %s\n", cudaGetErrorString(err));
        return 1;
    }

    err = cudaDeviceSynchronize();
    if (err != cudaSuccess) {
        printf("CUDA execution error: %s\n", cudaGetErrorString(err));
        return 1;
    }

    return 0;
}
