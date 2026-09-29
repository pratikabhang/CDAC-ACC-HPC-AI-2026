"""
Demo 03: Threads vs Processes — Concurrency Fundamentals
==========================================================

A single comprehensive demo covering all concurrency concepts:
    - Creating threads (shared PID, unique TIDs, shared memory)
    - Creating processes (unique PIDs, isolated memory)
    - The GIL: CPU-bound vs I/O-bound behavior
    - Race conditions and fixing them with Locks
    - Process memory isolation vs explicit shared memory (Value)

Uncomment one function at a time in main() to demonstrate progressively.
"""

import threading
import multiprocessing
import os
import time


# ===================================================================
# Worker functions — at module level for macOS/Windows 'spawn' compat
# ===================================================================

def cpu_task(n=5_000_000):
    """CPU-intensive calculation: sum of squares."""
    total = 0
    for i in range(n):
        total += i * i
    return total


def io_task(duration=1.0):
    """Simulate an I/O operation (network request, file read, etc.)."""
    time.sleep(duration)


def try_modify_global(label):
    """Attempt to modify a global variable from a child process."""
    global global_var
    global_var += 100
    print(f"  [Child '{label}', PID {os.getpid()}] "
          f"global_var inside child = {global_var}")


def increment_shared(counter, n):
    """Safely increment a multiprocessing.Value counter."""
    for _ in range(n):
        with counter.get_lock():
            counter.value += 1


# Global used in demo_process_isolation — each child gets its own copy
global_var = 0

NUM_WORKERS = 4
INCREMENTS = 500_000


# ===================================================================
# Demo 1: Threads — same PID, shared memory
# ===================================================================

def demo_threads_basics():
    """
    Show that threads live inside the same process:
    - All threads share the same PID.
    - Each thread has a unique thread ID (TID).
    - Threads can read/write the same shared list directly.
    """
    print("=" * 60)
    print("THREADS: Same PID, shared memory")
    print("=" * 60)

    print(f"Main thread → PID={os.getpid()}, TID={threading.get_ident()}\n")

    shared_results = []  # all threads will write to this list

    def worker(name, value):
        tid = threading.get_ident()
        result = value ** 2
        shared_results.append((name, result))
        print(f"  [{name}] PID={os.getpid()}, TID={tid} → {value}² = {result}")

    threads = []
    for i, name in enumerate(["Alpha", "Beta", "Gamma", "Delta"]):
        t = threading.Thread(target=worker, args=(name, i + 2))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"\nShared results (read from main thread): {shared_results}")
    print("→ All threads share the SAME memory space.\n")


# ===================================================================
# Demo 2: Processes — different PIDs, isolated memory
# ===================================================================

def demo_processes_basics():
    """
    Show that each process has its own PID and memory space.
    A child modifying a global variable does NOT affect the parent.
    """
    print("=" * 60)
    print("PROCESSES: Different PIDs, isolated memory")
    print("=" * 60)

    print(f"Parent PID: {os.getpid()}, global_var = {global_var}\n")

    p1 = multiprocessing.Process(target=try_modify_global, args=("Worker-A",))
    p2 = multiprocessing.Process(target=try_modify_global, args=("Worker-B",))
    p1.start(); p2.start()
    p1.join();  p2.join()

    print(f"\n  [Parent, PID {os.getpid()}] global_var = {global_var}")
    print("→ Parent's global_var is UNCHANGED — each process has its own copy.")
    print()

    # Now show multiprocessing.Value for explicit sharing
    print("Fix: Use multiprocessing.Value for shared state:")
    shared_counter = multiprocessing.Value('i', 0)

    procs = []
    for _ in range(5):
        p = multiprocessing.Process(
            target=increment_shared,
            args=(shared_counter, INCREMENTS)
        )
        procs.append(p)
        p.start()
    for p in procs:
        p.join()

    expected = 5 * INCREMENTS
    print(f"  Shared counter = {shared_counter.value}  (expected {expected})")
    print(f"  {'✓ Correct!' if shared_counter.value == expected else '✗ Wrong!'}\n")


# ===================================================================
# Demo 3: The GIL — CPU-bound vs I/O-bound
# ===================================================================

def demo_gil():
    """
    Show the GIL's impact:
    - CPU-bound: threads ≈ sequential (GIL serializes), processes give speedup.
    - I/O-bound: threads give speedup (GIL released during I/O).
    """
    print("=" * 60)
    print("THE GIL: CPU-Bound vs I/O-Bound")
    print("=" * 60)
    print(f"Workers: {NUM_WORKERS},  CPU cores: {multiprocessing.cpu_count()}\n")

    def run_sequential(task, n):
        for _ in range(n):
            task()

    def run_threaded(task, n):
        threads = [threading.Thread(target=task) for _ in range(n)]
        [t.start() for t in threads]
        [t.join() for t in threads]

    def run_multiprocess(task, n):
        procs = [multiprocessing.Process(target=task) for _ in range(n)]
        for p in procs: p.start()
        for p in procs: p.join()

    def benchmark(label, task):
        print(f"  ── {label} ({NUM_WORKERS} tasks) ──")

        start = time.time()
        run_sequential(task, NUM_WORKERS)
        t_seq = time.time() - start

        start = time.time()
        run_threaded(task, NUM_WORKERS)
        t_thr = time.time() - start

        start = time.time()
        run_multiprocess(task, NUM_WORKERS)
        t_proc = time.time() - start

        print(f"  Sequential   : {t_seq:.3f}s")
        print(f"  Threaded     : {t_thr:.3f}s  "
              f"(speedup: {t_seq/t_thr:.2f}x)")
        print(f"  Multiprocess : {t_proc:.3f}s  "
              f"(speedup: {t_seq/t_proc:.2f}x)")
        print()

    benchmark("CPU-BOUND  (sum of squares)", cpu_task)
    benchmark("I/O-BOUND  (simulated network)", io_task)

    print("TAKEAWAY:")
    print("  • CPU-bound → use multiprocessing  (threads blocked by GIL)")
    print("  • I/O-bound → threads work great    (GIL released during I/O)\n")


# ===================================================================
# Demo 4: Race conditions and Locks
# ===================================================================

def demo_race_condition():
    """
    Show that unsynchronized threads cause race conditions,
    and that threading.Lock fixes them.
    """
    print("=" * 60)
    print("RACE CONDITIONS & LOCKS")
    print("=" * 60)

    expected = 5 * INCREMENTS

    # ── Part A: WITHOUT Lock (race condition) ──
    counter_unsafe = 0

    def increment_unsafe(n):
        nonlocal counter_unsafe
        for _ in range(n):
            counter_unsafe += 1       # NOT atomic: read → add → write

    threads = [threading.Thread(target=increment_unsafe, args=(INCREMENTS,))
               for _ in range(5)]
    for t in threads: t.start()
    for t in threads: t.join()

    print(f"  WITHOUT Lock: counter = {counter_unsafe}  (expected {expected})")
    print(f"  {'✓ Correct' if counter_unsafe == expected else '✗ RACE CONDITION — value is wrong!'}")
    print()

    # ── Part B: WITH Lock (safe) ──
    counter_safe = 0
    lock = threading.Lock()

    def increment_safe(n):
        nonlocal counter_safe
        for _ in range(n):
            with lock:
                counter_safe += 1

    threads = [threading.Thread(target=increment_safe, args=(INCREMENTS,))
               for _ in range(5)]
    for t in threads: t.start()
    for t in threads: t.join()

    print(f"  WITH Lock   : counter = {counter_safe}  (expected {expected})")
    print(f"  {'✓ Correct!' if counter_safe == expected else '✗ Still wrong?!'}")
    print()
    print("TAKEAWAY: Always protect shared mutable state with a Lock.\n")


# ===================================================================
# Main: uncomment one function at a time to demonstrate progressively
# ===================================================================

def main():
    # demo_threads_basics()
    # demo_processes_basics()
    # demo_gil()
    demo_race_condition()


if __name__ == "__main__":
    main()
