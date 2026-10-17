#include <stdio.h>
#include <stdlib.h>
#include <cuda_runtime.h>
#include <time.h>

#define IDX(r, c, n) ((r) * (n) + (c))

__global__ void matMulGPU(const float *A, const float *B, float *C, int n) {
    int col = blockIdx.x * blockDim.x + threadIdx.x;
    int row = blockIdx.y * blockDim.y + threadIdx.y;
    if (row < n && col < n) {
        float sum = 0.0f;
        for (int k = 0; k < n; k++)
            sum += A[IDX(row, k, n)] * B[IDX(k, col, n)];
        C[IDX(row, col, n)] = sum;
    }
}

void matMulCPU(const float *A, const float *B, float *C, int n) {
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
            float sum = 0.0f;
            for (int k = 0; k < n; k++)
                sum += A[IDX(i, k, n)] * B[IDX(k, j, n)];
            C[IDX(i, j, n)] = sum;
        }
}

double elapsed_ms(clock_t start, clock_t end) {
    return 1000.0 * (double)(end - start) / CLOCKS_PER_SEC;
}

int main(int argc, char **argv) {
    int n = (argc > 1) ? atoi(argv[1]) : 256;
    if (n < 1) {
        printf("Matrix size must be positive.\\n");
        return 1;
    }
    size_t bytes = (size_t)n * n * sizeof(float);
    float *A = (float *)malloc(bytes), *B = (float *)malloc(bytes);
    float *Ccpu = (float *)malloc(bytes), *Cgpu = (float *)malloc(bytes);
    if (!A || !B || !Ccpu || !Cgpu) {
        printf("Host memory allocation failed.\\n");
        free(A); free(B); free(Ccpu); free(Cgpu);
        return 1;
    }
    for (int i = 0; i < n*n; i++) {
        A[i] = (float)((i % 7) + 1) / 7.0f;
        B[i] = (float)((i % 5) + 1) / 5.0f;
    }

    clock_t cpu_start = clock();
    matMulCPU(A, B, Ccpu, n);
    clock_t cpu_end = clock();
    double cpu_ms = elapsed_ms(cpu_start, cpu_end);

    float *dA = NULL, *dB = NULL, *dC = NULL;
    cudaError_t err = cudaMalloc(&dA, bytes);
    if (err == cudaSuccess) err = cudaMalloc(&dB, bytes);
    if (err == cudaSuccess) err = cudaMalloc(&dC, bytes);
    if (err != cudaSuccess) {
        printf("CUDA allocation failed: %s\\n", cudaGetErrorString(err));
        if (dA) cudaFree(dA); if (dB) cudaFree(dB); if (dC) cudaFree(dC);
        free(A); free(B); free(Ccpu); free(Cgpu);
        return 1;
    }

    cudaMemcpy(dA, A, bytes, cudaMemcpyHostToDevice);
    cudaMemcpy(dB, B, bytes, cudaMemcpyHostToDevice);
    dim3 threads(16, 16);
    dim3 blocks((n + threads.x - 1) / threads.x,
                (n + threads.y - 1) / threads.y);

    // Warm-up and synchronize before timing.
    matMulGPU<<<blocks, threads>>>(dA, dB, dC, n);
    err = cudaGetLastError();
    if (err == cudaSuccess) err = cudaDeviceSynchronize();
    if (err != cudaSuccess) {
        printf("CUDA kernel failed: %s\\n", cudaGetErrorString(err));
        cudaFree(dA); cudaFree(dB); cudaFree(dC);
        free(A); free(B); free(Ccpu); free(Cgpu);
        return 1;
    }

    cudaEvent_t start, stop;
    cudaEventCreate(&start); cudaEventCreate(&stop);
    cudaEventRecord(start);
    matMulGPU<<<blocks, threads>>>(dA, dB, dC, n);
    cudaEventRecord(stop);
    cudaEventSynchronize(stop);
    float gpu_kernel_ms = 0.0f;
    cudaEventElapsedTime(&gpu_kernel_ms, start, stop);
    cudaMemcpy(Cgpu, dC, bytes, cudaMemcpyDeviceToHost);

    int correct = 1;
    for (int i = 0; i < n*n; i++) {
        float diff = Ccpu[i] - Cgpu[i];
        if (diff < -0.001f || diff > 0.001f) { correct = 0; break; }
    }

    printf("Matrix size: %d x %d\\n", n, n);
    printf("CPU multiplication time: %.3f ms\\n", cpu_ms);
    printf("GPU kernel time (excludes transfers): %.3f ms\\n", gpu_kernel_ms);
    printf("Result check: %s\\n", correct ? "PASS" : "FAIL");
    if (gpu_kernel_ms > 0.0f)
        printf("CPU time / GPU kernel time: %.2f x (kernel-only comparison)\\n",
               cpu_ms / gpu_kernel_ms);

    cudaEventDestroy(start); cudaEventDestroy(stop);
    cudaFree(dA); cudaFree(dB); cudaFree(dC);
    free(A); free(B); free(Ccpu); free(Cgpu);
    return correct ? 0 : 1;
}
