"""
Demo: Process Communication (Queue, Pipe) and Pools
"""
import multiprocessing
import time
import os

# -----------------------------------------------------------------------------
# Module-level worker functions (Required for macOS 'spawn' start method)
# -----------------------------------------------------------------------------

def producer_worker(queue, name, items):
    """Puts items into the shared queue."""
    for item in items:
        msg = f"{name} produced {item}"
        print(f"[Producer {name}] -> {item}")
        queue.put(msg)
        time.sleep(0.1)

def consumer_worker(queue, num_expected):
    """Gets items from the shared queue."""
    for _ in range(num_expected):
        msg = queue.get()
        print(f"[Consumer] Received: {msg}")

def pipe_child_worker(conn):
    """Receives a message via pipe and sends a response."""
    print("[Child] Waiting for data from pipe...")
    msg = conn.recv()
    print(f"[Child] Received: {msg}")
    
    response = f"Hello from Child PID {os.getpid()}"
    print(f"[Child] Sending: {response}")
    conn.send(response)
    conn.close()

def square_number(n):
    """Simple worker for map/async demo."""
    time.sleep(0.1) # Simulate work
    return n * n

def async_callback(result):
    """Callback triggered when apply_async completes."""
    print(f"[Callback] Result computed: {result}")

# -----------------------------------------------------------------------------
# Demo execution functions
# -----------------------------------------------------------------------------

def demo_queue():
    print("--- Demo: Process Queue ---")
    q = multiprocessing.Queue()
    
    # 2 producers, 1 consumer
    p1 = multiprocessing.Process(target=producer_worker, args=(q, "P1", [1, 2, 3]))
    p2 = multiprocessing.Process(target=producer_worker, args=(q, "P2", [4, 5, 6]))
    c1 = multiprocessing.Process(target=consumer_worker, args=(q, 6))
    
    p1.start()
    p2.start()
    c1.start()
    
    p1.join()
    p2.join()
    c1.join()
    print("Done.\n")

def demo_pipe():
    print("--- Demo: Process Pipe ---")
    parent_conn, child_conn = multiprocessing.Pipe()
    
    p = multiprocessing.Process(target=pipe_child_worker, args=(child_conn,))
    p.start()
    
    print("[Parent] Sending data to child...")
    parent_conn.send("Hello from Parent")
    
    print("[Parent] Waiting for response...")
    response = parent_conn.recv()
    print(f"[Parent] Received response: {response}")
    
    p.join()
    print("Done.\n")

def demo_pool_map():
    print("--- Demo: Pool.map ---")
    numbers = [1, 2, 3, 4, 5]
    
    # Create a pool with 3 worker processes
    with multiprocessing.Pool(processes=3) as pool:
        print(f"Submitting numbers: {numbers}")
        # map() blocks until all results are ready
        results = pool.map(square_number, numbers)
        print(f"Results: {results}")
    print("Done.\n")

def demo_pool_async():
    print("--- Demo: Pool.apply_async ---")
    
    with multiprocessing.Pool(processes=2) as pool:
        print("Submitting task asynchronously...")
        # apply_async() does not block
        result_obj = pool.apply_async(
            square_number, 
            args=(10,), 
            callback=async_callback
        )
        print("Task submitted. Main process is free to do other things.")
        
        # Explicitly wait for the result here
        final_result = result_obj.get()
        print(f"Main process retrieved final result: {final_result}")
    print("Done.\n")

if __name__ == '__main__':
    # Uncomment the function you want to test
    demo_queue()
    # demo_pipe()
    # demo_pool_map()
    # demo_pool_async()
