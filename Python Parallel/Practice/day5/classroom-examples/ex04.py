import numpy as np
import pyopencl as cl

N = 1024

a_host = np.arange(N, dtype=np.float32) * 45
b_host = np.arange(N, dtype=np.float32) * 12
c_host = np.empty_like(a_host)

ctx = cl.create_some_context(interactive=False)
queue = cl.CommandQueue(ctx)

kernel_code = """
__kernel void vector_add(__global const float *a,
			__global const float *b,
			__global float *c) {
	int gid = get_global_id(0);
	c[gid] = a[gid] + b[gid];
}
"""

prg = cl.Program(ctx, kernel_code).build()

# create device variables (buffers)
mf = cl.mem_flags
a_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, a_host.nbytes, hostbuf=a_host)
b_buf = cl.Buffer(ctx, mf.READ_ONLY | mf.COPY_HOST_PTR, b_host.nbytes, hostbuf=b_host)
c_buf = cl.Buffer(ctx, mf.WRITE_ONLY, c_host.nbytes)

prg.vector_add(queue, (N, ), None, a_buf, b_buf, c_buf)

cl.enqueue_copy(queue, c_host, c_buf)




print("Kernel executed successfully")
print("Sample input a:", a_host[:5])
print("Sample input b:", b_host[:5])
print("Sample result c:", c_host[:5])

assert np.allclose(c_host, a_host + b_host), "Verfication succeeded"
print("All is well")
