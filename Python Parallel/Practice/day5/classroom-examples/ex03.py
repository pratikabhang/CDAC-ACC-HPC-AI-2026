import numpy as np
from numba import cuda


@cuda.jit # compiles this functon into C function when kernel is launched
def vector_add(a, b, c):
    idx = cuda.grid(1)
    if(idx < c.size):
        c[idx] = a[idx] + b[idx]


N = 100_000

# create host variables (CPU)
a = np.ones(N, dtype=np.float32) * 10.0
b = np.ones(N, dtype=np.float32) * 23.0
c = np.empty_like(a)

# create similar variables in GPU, and copy from host
d_a = cuda.to_device(a)
d_b = cuda.to_device(b)
d_c = cuda.device_array_like(a)

threads_per_block = 256
blocks_per_grid =  1024

# launch the kernel with the JIT compiled python code
vector_add[blocks_per_grid, threads_per_block](d_a, d_b, d_c)

c = d_c.copy_to_host()


print("Kernel executed successfully")
print("Sample input a:", a[:5])
print("Sample input b:", b[:5])
print("Sample result c:", c[:5])

assert np.allclose(c, a+b), "Verfication succeeded"
print("All is well")
