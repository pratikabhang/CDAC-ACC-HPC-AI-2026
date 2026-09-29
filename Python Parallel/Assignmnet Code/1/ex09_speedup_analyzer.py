import multiprocessing
import os
import random
import time

def monte_carlo_pi(num_samples):
    inside = 0
    for _ in range(num_samples):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1.0:
            inside += 1
    return inside

if __name__ == "__main__":
    total_samples = 5_000_000
    serial_fraction = 0.03
    max_cores = os.cpu_count() or 4
    worker_counts = [1, 2, 4, max_cores]

    start_seq = time.perf_counter()
    seq_inside = monte_carlo_pi(total_samples)
    seq_time = time.perf_counter() - start_seq
    seq_pi = 4 * seq_inside / total_samples

    print("Workers | Time(s)  | Speedup | Efficiency | Amdahl | Gustafson | Pi Estimate")
    print("-" * 75)
    print(f"1       | {seq_time:.3f}    | 1.00    | 100.0%     | 1.00   | 1.00      | {seq_pi:.5f}")

    for n in worker_counts:
        if n == 1:
            continue
        samples_per_worker = total_samples // n
        start_par = time.perf_counter()
        with multiprocessing.Pool(processes=n) as pool:
            results = pool.map(monte_carlo_pi, [samples_per_worker] * n)
        par_time = time.perf_counter() - start_par
        
        total_inside = sum(results)
        pi_estimate = 4 * total_inside / (samples_per_worker * n)
        speedup = seq_time / par_time if par_time > 0 else 0
        efficiency = (speedup / n) * 100
        amdahl = 1 / (serial_fraction + (1 - serial_fraction) / n)
        gustafson = n - serial_fraction * (n - 1)
        
        print(f"{n:<7} | {par_time:.3f}    | {speedup:.2f}    | {efficiency:.1f}%     | {amdahl:.2f}   | {gustafson:.2f}      | {pi_estimate:.5f}")