import os
import numpy as np
import pycuda.autoinit
import pycuda.driver as cuda
from pycuda.compiler import SourceModule

kernel_code = r"""
__global__ void vector_add(float *c,
                           const float *a,
                           const float *b,
                           int len) {
    int idx = blockDim.x * blockIdx.x + threadIdx.x;

    if (idx < len) {
        c[idx] = a[idx] + b[idx];
    }
}
"""

N = 1024

# Allocate host memory
a_host = np.arange(N, dtype=np.float32)
b_host = np.arange(N, dtype=np.float32) * 2.0
c_host = np.empty_like(a_host)

# Compile the CUDA kernel
mod = SourceModule(kernel_code, options=["-ccbin", os.popen("which g++").read().strip()])
vector_add = mod.get_function("vector_add")

# Allocate GPU memory
a_gpu = cuda.mem_alloc(a_host.nbytes)
b_gpu = cuda.mem_alloc(b_host.nbytes)
c_gpu = cuda.mem_alloc(c_host.nbytes)

# Copy inputs from host to GPU
cuda.memcpy_htod(a_gpu, a_host)
cuda.memcpy_htod(b_gpu, b_host)

block_size = 256
grid_size = (N + block_size - 1) // block_size

# Execute the kernel
vector_add(
    c_gpu,
    a_gpu,
    b_gpu,
    np.int32(N),
    block=(block_size, 1, 1),
    grid=(grid_size, 1, 1)
)

# Copy results from GPU to host
cuda.memcpy_dtoh(c_host, c_gpu)

# Verify results
expected = a_host + b_host

print("Kernel executed successfully")
print("Sample input a:", a_host[:5])
print("Sample input b:", b_host[:5])
print("Sample result c:", c_host[:5])
print("All results correct:", np.allclose(c_host, expected))
