"""
Demo 04: Parallel Performance — Pool, Speedup & Amdahl's Law
===============================================================

A single comprehensive demo covering all performance concepts:
    - multiprocessing.Pool.map() for data parallelism
    - Sequential vs parallel comparison
    - Speedup and Efficiency metrics
    - Amdahl's Law (theoretical upper bound)
    - Gustafson's Law (scaled speedup)

Uncomment one function at a time in main() to demonstrate progressively.
"""

import multiprocessing
import time


# ===================================================================
# Worker functions — at module level for macOS/Windows 'spawn' compat
# ===================================================================

def is_prime(n):
    """Check if n is prime using trial division."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def count_primes(limit):
    """Count primes up to `limit` — CPU-heavy, ideal for parallelism."""
    count = 0
    for i in range(2, limit):
        if is_prime(i):
            count += 1
    return (limit, count)


def cpu_work(iterations):
    """Pure CPU work: sum of squares (used for Amdahl benchmarks)."""
    total = 0
    for i in range(iterations):
        total += i * i
    return total


# ===================================================================
# Helpers
# ===================================================================

def get_worker_counts(max_cores):
    """Build worker counts: 1, 2, 4, … up to max_cores."""
    counts = []
    n = 1
    while n <= max_cores:
        counts.append(n)
        n *= 2
    if counts[-1] != max_cores:
        counts.append(max_cores)
    return counts


def amdahl_speedup(serial_fraction, num_processors):
    """
    Amdahl's Law: theoretical maximum speedup.

    Formula:  S(N) = 1 / (s + (1-s)/N)
        s = serial fraction (0..1)
        N = number of processors
    """
    return 1.0 / (serial_fraction + (1.0 - serial_fraction) / num_processors)


# ===================================================================
# Demo 1: Pool.map() — data parallelism made simple
# ===================================================================

def demo_pool_map():
    """
    Use multiprocessing.Pool.map() to distribute identical tasks
    across workers and observe real parallel speedup.
    """
    print("=" * 60)
    print("POOL.MAP() — Data Parallelism")
    print("=" * 60)

    tasks = [200_000] * 16   # 16 identical heavy tasks
    num_workers = multiprocessing.cpu_count()

    print(f"Task       : Count primes up to 200,000 × 16 times")
    print(f"CPU cores  : {num_workers}")
    print()

    # Sequential
    start = time.time()
    seq_results = [count_primes(n) for n in tasks]
    t_seq = time.time() - start
    print(f"Sequential : {t_seq:.3f}s")

    # Parallel
    start = time.time()
    with multiprocessing.Pool(processes=num_workers) as pool:
        par_results = pool.map(count_primes, tasks)
    t_par = time.time() - start
    print(f"Parallel   : {t_par:.3f}s  ({num_workers} workers)")

    # Verify
    assert seq_results == par_results, "Results mismatch!"
    print(f"Results    : each task found {seq_results[0][1]} primes ✓")

    if t_par > 0:
        speedup = t_seq / t_par
        efficiency = speedup / num_workers
        print(f"\nSpeedup    : {speedup:.2f}x")
        print(f"Efficiency : {efficiency:.1%}")
    print()


# ===================================================================
# Demo 2: Speedup & Efficiency across varying core counts
# ===================================================================

def demo_speedup_efficiency():
    """
    Measure sequential vs parallel runtime across 1, 2, 4, … N cores.
    Compute actual Speedup = T_seq / T_par and Efficiency = Speedup / N.
    """
    print("=" * 60)
    print("SPEEDUP & EFFICIENCY — Scaling with Core Count")
    print("=" * 60)

    TOTAL = 10_000_000
    max_cores = multiprocessing.cpu_count()
    worker_counts = get_worker_counts(max_cores)

    print(f"Workload       : sum of squares, {TOTAL:,} iterations")
    print(f"Available cores: {max_cores}")
    print()

    # Sequential baseline
    start = time.time()
    cpu_work(TOTAL)
    t_seq = time.time() - start
    print(f"Sequential     : {t_seq:.3f}s\n")

    header = f"{'N':>5} {'Time':>8} {'Speedup':>8} {'Efficiency':>11}"
    print(header)
    print("─" * len(header))

    for n in worker_counts:
        chunk = TOTAL // n
        start = time.time()
        with multiprocessing.Pool(n) as pool:
            pool.map(cpu_work, [chunk] * n)
        t_par = time.time() - start

        s = t_seq / t_par
        e = s / n
        print(f"{n:>5} {t_par:>8.3f} {s:>8.2f} {e:>10.1%}")

    print()
    print("KEY:")
    print("  Speedup(N)    = T_seq / T_par(N)")
    print("  Efficiency(N) = Speedup(N) / N   (ideal = 100%)\n")


# ===================================================================
# Demo 3: Amdahl's Law & Gustafson's Law
# ===================================================================

def demo_amdahl_gustafson():
    """
    Compare empirical speedup against theoretical bounds:
    - Amdahl's Law  (fixed problem size, pessimistic)
    - Gustafson's Law (scaled problem size, optimistic)
    """
    print("=" * 60)
    print("AMDAHL'S LAW & GUSTAFSON'S LAW")
    print("=" * 60)

    TOTAL = 10_000_000
    max_cores = multiprocessing.cpu_count()
    worker_counts = get_worker_counts(max_cores)
    S = 0.05  # assumed serial fraction (5%)

    print(f"Serial fraction (S) : {S:.0%}")
    print(f"Amdahl max (N→∞)    : {1.0/S:.1f}x")
    print()

    # Sequential baseline
    start = time.time()
    cpu_work(TOTAL)
    t_seq = time.time() - start
    print(f"Sequential time     : {t_seq:.3f}s\n")

    header = (f"{'N':>5} {'Time':>7} {'Actual':>7} "
              f"{'Amdahl':>7} {'Gustafson':>10}")
    print(header)
    print("─" * len(header))

    for n in worker_counts:
        chunk = TOTAL // n
        start = time.time()
        with multiprocessing.Pool(n) as pool:
            pool.map(cpu_work, [chunk] * n)
        t_par = time.time() - start

        actual   = t_seq / t_par
        amdahl   = amdahl_speedup(S, n)
        gustafson = n - S * (n - 1)

        print(f"{n:>5} {t_par:>7.3f} {actual:>7.2f} "
              f"{amdahl:>7.2f} {gustafson:>10.2f}")

    print()
    print("Amdahl's Law   : S(N) = 1 / (s + (1-s)/N)")
    print("  → Fixed problem size. Even with ∞ cores, speedup ≤ 1/s.")
    print()
    print("Gustafson's Law: S(N) = N - s × (N - 1)")
    print("  → Scale problem size with N. Speedup grows nearly linearly.")
    print()


# ===================================================================
# Main: uncomment one function at a time to demonstrate progressively
# ===================================================================

def main():
    demo_pool_map()
    # demo_speedup_efficiency()
    # demo_amdahl_gustafson()


if __name__ == "__main__":
    main()
