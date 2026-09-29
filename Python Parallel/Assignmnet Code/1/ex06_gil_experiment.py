import time
import threading
import multiprocessing

# 1. Heavy math (CPU-bound)
def heavy_math(n=28):
    if n <= 1:
        return n
    return heavy_math(n - 1) + heavy_math(n - 2)

# 2. Waiting around (I/O-bound, like downloading a file)
def fake_download(x):
    time.sleep(0.5)

# Helper function to test timing
def run_test(func, items, mode):
    start = time.perf_counter()
    
    if mode == "normal":
        for item in items:
            func(item)
    elif mode == "threads":
        threads = [threading.Thread(target=func, args=(item,)) for item in items]
        for t in threads: t.start()
        for t in threads: t.join()
    elif mode == "processes":
        procs = [multiprocessing.Process(target=func, args=(item,)) for item in items]
        for p in procs: p.start()
        for p in procs: p.join()
        
    return time.perf_counter() - start

if __name__ == "__main__":
    items_cpu = [28] * 4
    items_io = range(4)

    print("Heavy Math Test ")
    print(f"Normal (one by one): {run_test(heavy_math, items_cpu, 'normal'):.2f} seconds")
    print(f"Using Threads:       {run_test(heavy_math, items_cpu, 'threads'):.2f} seconds")
    print(f"Using Processes:     {run_test(heavy_math, items_cpu, 'processes'):.2f} seconds")

    print("\n Waiting/Download Test")
    print(f"Normal (one by one): {run_test(fake_download, items_io, 'normal'):.2f} seconds")
    print(f"Using Threads:       {run_test(fake_download, items_io, 'threads'):.2f} seconds")
    print(f"Using Processes:     {run_test(fake_download, items_io, 'processes'):.2f} seconds")