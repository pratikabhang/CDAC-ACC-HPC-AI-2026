#include <stdio.h>
#include <cuda_runtime.h>

__global__ void vectorAdd(const int *a, const int *b, int *c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        c[i] = a[i] + b[i];
    }
}

int main() {
    const int n = 8;
    int h_a[8] = {1, 2, 3, 4, 5, 6, 7, 8};
    int h_b[8] = {10, 20, 30, 40, 50, 60, 70, 80};
    int h_c[8];

    int *d_a = NULL, *d_b = NULL, *d_c = NULL;
    size_t bytes = n * sizeof(int);

    if (cudaMalloc(&d_a, bytes) != cudaSuccess ||
        cudaMalloc(&d_b, bytes) != cudaSuccess ||
        cudaMalloc(&d_c, bytes) != cudaSuccess) {
        printf("Device memory allocation failed.\n");
        return 1;
    }

    cudaMemcpy(d_a, h_a, bytes, cudaMemcpyHostToDevice);
    cudaMemcpy(d_b, h_b, bytes, cudaMemcpyHostToDevice);

    int threadsPerBlock = 256;
    int blocks = (n + threadsPerBlock - 1) / threadsPerBlock;
    vectorAdd<<<blocks, threadsPerBlock>>>(d_a, d_b, d_c, n);

    cudaError_t err = cudaGetLastError();
    if (err == cudaSuccess) err = cudaDeviceSynchronize();
    if (err != cudaSuccess) {
        printf("CUDA error: %s\n", cudaGetErrorString(err));
        cudaFree(d_a); cudaFree(d_b); cudaFree(d_c);
        return 1;
    }

    cudaMemcpy(h_c, d_c, bytes, cudaMemcpyDeviceToHost);
    printf("Vector addition result: ");
    for (int i = 0; i < n; i++) printf("%d ", h_c[i]);
    printf("\n");

    cudaFree(d_a); cudaFree(d_b); cudaFree(d_c);
    return 0;
}
