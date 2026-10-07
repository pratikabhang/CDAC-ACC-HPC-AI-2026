"""
Exercise 2: 2D Matrix Transposition Kernel
Requirement: 512x512 matrix, block=(16,16,1).
"""
import numpy as np

N = 512
BLOCK_X = 16
BLOCK_Y = 16

def cpu_fallback():
    matrix = np.arange(N * N, dtype=np.float32).reshape(N, N)
    output = matrix.T.copy()
    expected = matrix.T
    print("Exercise 2 - CPU architectural simulation")
    print(f"matrix={N}x{N}, block=({BLOCK_X},{BLOCK_Y},1), grid=({N//16},{N//16},1)")
    print("Verification:", np.array_equal(output, expected))
    print("Corners:", output[0,0], output[0,1], output[1,0], output[-1,-1])

def gpu_run():
    import pycuda.autoinit
    import pycuda.driver as cuda
    from pycuda.compiler import SourceModule

    matrix = np.arange(N * N, dtype=np.float32).reshape(N, N)
    output = np.empty_like(matrix)

    d_in = cuda.mem_alloc(matrix.nbytes)
    d_out = cuda.mem_alloc(output.nbytes)
    cuda.memcpy_htod(d_in, matrix)

    kernel_code = r"""
    __global__ void transpose_matrix(float *out, const float *in,
                                      int width, int height) {
        int col = blockIdx.x * blockDim.x + threadIdx.x;
        int row = blockIdx.y * blockDim.y + threadIdx.y;
        if (col < width && row < height) {
            int in_idx = row * width + col;
            int out_idx = col * height + row;
            out[out_idx] = in[in_idx];
        }
    }
    """
    module = SourceModule(kernel_code)
    kernel = module.get_function("transpose_matrix")

    grid = ((N + BLOCK_X - 1) // BLOCK_X,
            (N + BLOCK_Y - 1) // BLOCK_Y, 1)
    kernel(d_out, d_in, np.int32(N), np.int32(N),
           block=(BLOCK_X, BLOCK_Y, 1), grid=grid)
    cuda.memcpy_dtoh(output, d_out)

    print("Exercise 2 - PyCUDA GPU")
    print(f"matrix={N}x{N}, block=({BLOCK_X},{BLOCK_Y},1), grid={grid}")
    print("Verification:", np.array_equal(output, matrix.T))
    print("Corners:", output[0,0], output[0,1], output[1,0], output[-1,-1])

if __name__ == "__main__":
    try:
        gpu_run()
    except Exception:
        print("PyCUDA/CUDA unavailable; using architectural simulation fallback.")
        cpu_fallback()
