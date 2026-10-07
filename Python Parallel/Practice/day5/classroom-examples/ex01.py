import pycuda.driver as cuda

cuda.init()

num_devices = cuda.Device.count()
print(f"Total CUDA GPUs detected: {num_devices}\n")

for i in range(num_devices):
  dev = cuda.Device(i)
  cc_maj, cc_min = dev.compute_capability()
  vram_gb = dev.total_memory() / (1024**3)
  sms = dev.get_attribute(cuda.device_attribute.MULTIPROCESSOR_COUNT)
  max_th = dev.get_attribute(cuda.device_attribute.MAX_THREADS_PER_BLOCK)

  print(f"---GPU#{i}: {dev.name()}---")
  print(f"Compute capability: ({cc_maj}, {cc_min})")
  print(f"Total VRAM: {vram_gb}GB")
  print(f"Multiprocessors: {sms}")
  print(f"Max number of threads per block: {max_th}")
  print()
