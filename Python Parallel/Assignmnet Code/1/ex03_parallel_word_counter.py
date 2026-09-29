import multiprocessing
import os
import time

# Worker function to count words in a file
def count_words(filepath):
    time.sleep(0.5)  # Simulate a slow disk read delay
    with open(filepath, "r", encoding="utf-8") as f:
        words = f.read().split()
    return filepath, len(words)

if __name__ == "__main__":
    files = [f"file_{i}.txt" for i in range(6)]
    
    # 1. Create sample test files
    for name in files:
        with open(name, "w", encoding="utf-8") as f:
            f.write("python parallel computing data performance " * 1500)

    # 2. Sequential Run
    start_seq = time.time()
    seq_results = [count_words(f) for f in files]
    seq_time = time.time() - start_seq
    print(f"Sequential Time: {seq_time:.2f} seconds")

    # 3. Parallel Run using Pool
    start_par = time.time()
    with multiprocessing.Pool() as pool:
        par_results = pool.map(count_words, files)
    par_time = time.time() - start_par
    print(f"Parallel Time:   {par_time:.2f} seconds")

    # 4. Print results & speedup
    print("\nResults:", par_results)
    print(f"Speedup: {seq_time / par_time:.2f}x")

    # 5. Clean up files
    for name in files:
        if os.path.exists(name):
            os.remove(name)