"""
Demo: Thread Synchronization Primitives
Covers: Lock, RLock, and Semaphore.
"""
import threading
import time

def demo_lock():
    print("\n--- Running demo_lock ---")
    counter = 0
    lock = threading.Lock()
    
    def worker():
        nonlocal counter
        for _ in range(100000):
            with lock:
                counter += 1
                
    threads = [threading.Thread(target=worker) for _ in range(5)]
    for t in threads: t.start()
    for t in threads: t.join()
    
    print(f"Final counter value: {counter} (expected 500000)")

def demo_rlock():
    print("\n--- Running demo_rlock ---")
    rlock = threading.RLock()
    
    def recursive_task(depth):
        if depth == 0:
            return
        with rlock:
            print(f"Thread {threading.current_thread().name} acquired lock at depth {depth}")
            recursive_task(depth - 1)
            
    t = threading.Thread(target=recursive_task, args=(3,), name="Worker")
    t.start()
    t.join()
    print("RLock demo finished.")

def demo_semaphore():
    print("\n--- Running demo_semaphore ---")
    sem = threading.Semaphore(3) # Max 3 concurrent accesses
    
    def worker(worker_id):
        print(f"Worker {worker_id} waiting...")
        with sem:
            print(f"Worker {worker_id} acquired resource.")
            time.sleep(0.5)
            print(f"Worker {worker_id} releasing resource.")
            
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(1, 6)]
    for t in threads: t.start()
    for t in threads: t.join()
    print("Semaphore demo finished.")

def main():
    demo_lock()
    # demo_rlock()
    # demo_semaphore()

if __name__ == '__main__':
    main()
