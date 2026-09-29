import threading
import random

data = [0, 0, 0, 0]
barrier = threading.Barrier(4)


def worker(i):
    try:
        # Phase 1
        data[i] = random.randint(10, 100)
        print(f"[Thread {i}] Phase 1 complete, waiting at barrier...")

        barrier.wait()

        # Phase 2
        total = sum(data)
        share = (data[i] / total) * 100

        print(f"[Thread {i}] Share of total: {share:.2f}%")

    except threading.BrokenBarrierError:
        print(f"[Thread {i}] Barrier was broken.")


if __name__ == "__main__":
    threads = []

    for i in range(4):
        thread = threading.Thread(target=worker, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Data:", data)
