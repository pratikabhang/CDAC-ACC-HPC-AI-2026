"""
Exercise 1: Distributed Scientific Computing with SCOOP.
Computes a Monte Carlo estimate of the integral of sin(x)*exp(-x)
on [0, pi], using 10,000,000 evaluations split into 16 chunks.
"""

import math
import random
import time
from scoop import futures

TOTAL_SAMPLES = 10_000_000
TASK_COUNT = 16
LOWER = 0.0
UPPER = math.pi


def evaluate_subrange(params):
    subrange_id, samples_count = params
    rng = random.Random(1000 + subrange_id)

    max_y = 1.0
    hits = 0

    for _ in range(samples_count):
        x = LOWER + (UPPER - LOWER) * rng.random()
        y = max_y * rng.random()
        curve_y = math.sin(x) * math.exp(-x)

        if y <= curve_y:
            hits += 1

    return {
        "subrange_id": subrange_id,
        "hits": hits,
        "total": samples_count,
    }


def main():
    base = TOTAL_SAMPLES // TASK_COUNT
    remainder = TOTAL_SAMPLES % TASK_COUNT

    task_workloads = []
    for task_id in range(TASK_COUNT):
        samples = base + (1 if task_id < remainder else 0)
        task_workloads.append((task_id, samples))

    start = time.perf_counter()
    results = list(futures.map(evaluate_subrange, task_workloads))
    distributed_time = time.perf_counter() - start

    total_hits = sum(item["hits"] for item in results)
    total_samples = sum(item["total"] for item in results)

    # Area of rectangle = pi * 1.0.
    estimate = (total_hits / total_samples) * math.pi

    print("\n--- SCOOP Distributed Monte Carlo ---")
    print(f"Total evaluations : {total_samples:,}")
    print(f"Task chunks       : {TASK_COUNT}")
    print(f"Estimated integral: {estimate:.8f}")
    print(f"Distributed time  : {distributed_time:.4f} seconds")

    start = time.perf_counter()
    sequential_results = [
        evaluate_subrange(item) for item in task_workloads
    ]
    sequential_time = time.perf_counter() - start

    seq_hits = sum(item["hits"] for item in sequential_results)
    seq_total = sum(item["total"] for item in sequential_results)
    seq_estimate = (seq_hits / seq_total) * math.pi

    print(f"Sequential estimate: {seq_estimate:.8f}")
    print(f"Sequential time    : {sequential_time:.4f} seconds")

    if distributed_time > 0:
        print(f"Time ratio (seq/dist): {sequential_time / distributed_time:.2f}x")


if __name__ == "__main__":
    main()
