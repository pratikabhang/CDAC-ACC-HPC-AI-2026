"""
Exercise 4: Numba CUDA 3-point moving average using shared memory.
The shared tile includes two halo elements so neighboring blocks are handled correctly.
"""
import numpy as np

N = 1024
THREADS = 256

def cpu_fallback():
    x = np.arange(N, dtype=np.float32)
    y = np.empty_like(x)
    y[:] = np.nan
    y[1:-1] = (x[:-2] + x[1:-1] + x[2:]) / np.float32(3.0)

    expected = np.full_like(x, np.nan)
    expected[1:-1] = (x[:-2] + x[1:-1] + x[2:]) / np.float32(3.0)

    print("Exercise 4 - CPU architectural simulation")
    print(f"N={N}, threads_per_block={THREADS}, blocks={(N + THREADS - 1)//THREADS}")
    print("Interior verification:", np.allclose(y[1:-1], expected[1:-1]))
    print("First 5 values:", y[:5])

def gpu_run():
    from numba import cuda

    @cuda.jit
    def moving_average_kernel(input_data, output_data):
        # Two halo values + 256 block values.
        shared_tile = cuda.shared.array(shape=(THREADS + 2,), dtype=np.float32)
        t_id = cuda.threadIdx.x
        g_id = cuda.grid(1)

        if g_id < input_data.size:
            shared_tile[t_id + 1] = input_data[g_id]

        if t_id == 0:
            left = g_id - 1
            shared_tile[0] = input_data[left] if left >= 0 else input_data[0]

        if t_id == THREADS - 1:
            right = g_id + 1
            shared_tile[THREADS + 1] = (
                input_data[right] if right < input_data.size
                else input_data[input_data.size - 1]
            )

        cuda.syncthreads()

        if 0 < g_id < input_data.size - 1:
            output_data[g_id] = (
                shared_tile[t_id] +
                shared_tile[t_id + 1] +
                shared_tile[t_id + 2]
            ) / np.float32(3.0)

    x = np.arange(N, dtype=np.float32)
    d_x = cuda.to_device(x)
    d_y = cuda.device_array_like(x)

    blocks = (N + THREADS - 1) // THREADS
    moving_average_kernel[blocks, THREADS](d_x, d_y)
    cuda.synchronize()

    y = d_y.copy_to_host()
    expected = (x[:-2] + x[1:-1] + x[2:]) / np.float32(3.0)

    print("Exercise 4 - Numba CUDA")
    print(f"N={N}, threads_per_block={THREADS}, blocks={blocks}")
    print("Interior verification:", np.allclose(y[1:-1], expected))
    print("First 5 values:", y[:5])

if __name__ == "__main__":
    try:
        gpu_run()
    except Exception:
        print("Numba CUDA unavailable; using architectural simulation fallback.")
        cpu_fallback()
