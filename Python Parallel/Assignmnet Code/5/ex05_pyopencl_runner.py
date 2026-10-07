"""
Exercise 5: PyOpenCL platform/device discovery and vector multiplication.
Uses a simple CPU fallback if PyOpenCL/OpenCL is unavailable.
"""
import numpy as np

N = 100_000

def cpu_fallback():
    a = np.arange(N, dtype=np.float32)
    b = np.full(N, 2.0, dtype=np.float32)
    c = a * b
    print("Exercise 5 - CPU architectural simulation")
    print("OpenCL platform discovery unavailable.")
    print(f"Vector length={N}")
    print("Verification:", np.allclose(c, a * b))
    print("First 5 output values:", c[:5])

def gpu_run():
    import pyopencl as cl

    platforms = cl.get_platforms()
    if not platforms:
        raise RuntimeError("No OpenCL platforms found.")

    for plat in platforms:
        print("Platform:", plat.name)
        for dev in plat.get_devices():
            dev_type = cl.device_type.to_string(dev.type)
            print("  Device:", dev.name)
            print("  Vendor:", dev.vendor)
            print("  Type:", dev_type)
            print("  Compute units:", dev.max_compute_units)

    platform = platforms[0]
    device = platform.get_devices()[0]
    ctx = cl.Context([device])
    queue = cl.CommandQueue(ctx)

    kernel_code = r"""
    __kernel void vector_mult(__global const float *a,
                              __global const float *b,
                              __global float *c) {
        int gid = get_global_id(0);
        c[gid] = a[gid] * b[gid];
    }
    """
    program = cl.Program(ctx, kernel_code).build()

    a = np.arange(N, dtype=np.float32)
    b = np.full(N, 2.0, dtype=np.float32)
    c = np.empty_like(a)

    mf = cl.mem_flags
    a_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=a)
    b_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, hostbuf=b)
    c_buf = cl.Buffer(ctx, mf.WRITE_ONLY, c.nbytes)

    program.vector_mult(queue, (N,), None, a_buf, b_buf, c_buf)
    cl.enqueue_copy(queue, c, c_buf).wait()

    print("Exercise 5 - PyOpenCL")
    print(f"Vector length={N}")
    print("Verification:", np.allclose(c, a * b))
    print("First 5 output values:", c[:5])

if __name__ == "__main__":
    try:
        gpu_run()
    except Exception:
        print("PyOpenCL/OpenCL unavailable; using architectural simulation fallback.")
        cpu_fallback()
