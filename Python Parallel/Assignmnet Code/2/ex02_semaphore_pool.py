import threading
import time
import random

semaphore = threading.Semaphore(3)
active_connections = 0
lock = threading.Lock()


def worker(worker_id):
    global active_connections

    with semaphore:
        with lock:
            active_connections += 1
            active = active_connections

        print(f"[Worker {worker_id}] Connected to Database "
              f"(active slots: {active})")

        time.sleep(random.uniform(0.3, 0.8))

        print(f"[Worker {worker_id}] Finished query, releasing connection")

        with lock:
            active_connections -= 1


if __name__ == "__main__":
    threads = []

    for i in range(1, 11):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All workers finished.")
