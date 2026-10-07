"""
Exercise 1: PyCUDA Vector Scaling & Memory Management
Requirement: 65,536 float32 elements, alpha=3.5, block=256.
Includes a CPU architectural simulation fallback when CUDA/PyCUDA is unavailable.
"""
import numpy as np

N = 65536
ALPHA = np.float32(3.5)
BLOCK = 256

def cpu_fallback():
    # Same 5-step flow: host -> allocate -> copy -> kernel simulation -> host.
    x = np.arange(N, dtype=np.float32)
    y = np.empty_like(x)
    device_x = x.copy()
    device_y = np.empty_like(x)
    device_y[:] = ALPHA * device_x
    y[:] = device_y
    expected = ALPHA * x
    print("Exercise 1 - CPU architectural simulation")
    print(f"N={N}, alpha={ALPHA}, block={BLOCK}, grid={N // BLOCK}")
    print("Verification:", np.allclose(y, expected))
    print("First 5 output values:", y[:5])

def gpu_run():
    import pycuda.autoinit
    import pycuda.driver as cuda
    from pycuda.compiler import SourceModule

    x = np.arange(N, dtype=np.float32)
    y = np.empty_like(x)
    x_gpu = cuda.mem_alloc(x.nbytes)
    y_gpu = cuda.mem_alloc(y.nbytes)

    cuda.memcpy_htod(x_gpu, x)

    kernel_code = r"""
    __global__ void scale_vector(float *y, const float *x, float alpha, int n) {
        int idx = blockDim.x * blockIdx.x + threadIdx.x;
        if (idx < n) {
            y[idx] = alpha * x[idx];
        }
    }
    """
    module = SourceModule(kernel_code)
    kernel = module.get_function("scale_vector")

    grid = (N + BLOCK - 1) // BLOCK
    kernel(y_gpu, x_gpu, ALPHA, np.int32(N),
           block=(BLOCK, 1, 1), grid=(grid, 1, 1))
    cuda.memcpy_dtoh(y, y_gpu)

    print("Exercise 1 - PyCUDA GPU")
    print(f"N={N}, alpha={ALPHA}, block={BLOCK}, grid={grid}")
    print("Verification:", np.allclose(y, ALPHA * x))
    print("First 5 output values:", y[:5])

if __name__ == "__main__":
    try:
        gpu_run()
    except Exception as exc:
        print("PyCUDA/CUDA unavailable; using required architectural simulation fallback.")
        cpu_fallback()
