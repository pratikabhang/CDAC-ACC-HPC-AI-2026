"""
Demo: Thread Coordination mechanisms
Covers: Condition, Event, Barrier, and Queue communication.
"""
import threading
import time
import queue

def demo_condition():
    print("\n--- Running demo_condition ---")
    cond = threading.Condition()
    items = []
    
    def producer():
        with cond:
            for i in range(5):
                items.append(f"item-{i}")
                print(f"Produced item-{i}")
            cond.notify() # Notify the consumer
            print("Producer finished.")
            
    def consumer():
        with cond:
            while not items:
                print("Consumer waiting...")
                cond.wait()
            print(f"Consumer got items: {items}")
            
    c = threading.Thread(target=consumer)
    p = threading.Thread(target=producer)
    c.start()
    time.sleep(0.1) # Let consumer wait
    p.start()
    c.join(); p.join()

def demo_event():
    print("\n--- Running demo_event ---")
    start_event = threading.Event()
    
    def worker(worker_id):
        print(f"Worker {worker_id} waiting for start signal...")
        start_event.wait()
        print(f"Worker {worker_id} started work!")
        
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
    for t in threads: t.start()
    
    time.sleep(1)
    print("Main signaling workers to start...")
    start_event.set()
    for t in threads: t.join()

def demo_barrier():
    print("\n--- Running demo_barrier ---")
    barrier = threading.Barrier(3)
    
    def worker(worker_id):
        print(f"Worker {worker_id} doing phase 1...")
        time.sleep(0.1 * worker_id)
        print(f"Worker {worker_id} waiting at barrier...")
        barrier.wait()
        print(f"Worker {worker_id} doing phase 2...")
        
    threads = [threading.Thread(target=worker, args=(i,)) for i in range(1, 4)]
    for t in threads: t.start()
    for t in threads: t.join()

def demo_queue_types():
    print("\n--- Running demo_queue_types ---")
    pq = queue.PriorityQueue()
    
    # Format: (priority, data)
    pq.put((3, "Medium priority task"))
    pq.put((1, "High priority task"))
    pq.put((5, "Low priority task"))
    
    def worker():
        while not pq.empty():
            priority, task = pq.get()
            print(f"Processing: {task} (Priority {priority})")
            pq.task_done()
            
    t = threading.Thread(target=worker)
    t.start()
    t.join()

def main():
    demo_condition()
    # demo_event()
    # demo_barrier()
    # demo_queue_types()

if __name__ == '__main__':
    main()
