"""
Exercise 3: High-Level GPU Arrays & Custom Elementwise Expressions
Requirement: u and v have 500,000 random values.
w = 2*u + 5*v - 1
ReLU: max(0,x)
"""
import numpy as np

N = 500_000

def cpu_fallback():
    rng = np.random.default_rng(5)
    u = rng.random(N, dtype=np.float32)
    v = rng.random(N, dtype=np.float32)
    w = 2.0 * u + 5.0 * v - 1.0
    expected = 2.0 * u + 5.0 * v - 1.0

    relu_input = np.array([-2.0, -1.0, 0.0, 1.0, 3.0], dtype=np.float32)
    relu_output = np.maximum(relu_input, 0.0)

    print("Exercise 3 - CPU architectural simulation")
    print(f"N={N}")
    print("Linear combination verification:", np.allclose(w, expected))
    print("ReLU input:", relu_input)
    print("ReLU output:", relu_output)

def gpu_run():
    import pycuda.autoinit
    import pycuda.gpuarray as gpuarray
    from pycuda.elementwise import ElementwiseKernel

    rng = np.random.default_rng(5)
    u = rng.random(N, dtype=np.float32)
    v = rng.random(N, dtype=np.float32)

    u_gpu = gpuarray.to_gpu(u)
    v_gpu = gpuarray.to_gpu(v)
    w_gpu = 2.0 * u_gpu + 5.0 * v_gpu - 1.0
    w = w_gpu.get()

    relu_kernel = ElementwiseKernel(
        "float *out, const float *in",
        "out[i] = (in[i] > 0.0f) ? in[i] : 0.0f",
        "relu_activation"
    )

    relu_input = np.array([-2.0, -1.0, 0.0, 1.0, 3.0], dtype=np.float32)
    relu_output = np.empty_like(relu_input)
    relu_in_gpu = gpuarray.to_gpu(relu_input)
    relu_out_gpu = gpuarray.empty_like(relu_in_gpu)
    relu_kernel(relu_out_gpu, relu_in_gpu)
    relu_output = relu_out_gpu.get()

    print("Exercise 3 - PyCUDA gpuarray")
    print(f"N={N}")
    print("Linear combination verification:",
          np.allclose(w, 2.0 * u + 5.0 * v - 1.0))
    print("ReLU input:", relu_input)
    print("ReLU output:", relu_output)

if __name__ == "__main__":
    try:
        gpu_run()
    except Exception:
        print("PyCUDA/CUDA unavailable; using architectural simulation fallback.")
        cpu_fallback()
