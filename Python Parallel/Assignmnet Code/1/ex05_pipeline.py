import queue
import random
import threading
import time

def generator(q1):
    for i in range(1, 6):  # producing 5 items for a quick demo
        item = {"id": i, "value": random.randint(1, 10)}
        q1.put(item)
        print(f"Generator created item: {item}")
        time.sleep(0.1)
    q1.put(None)  # stop signal

def processor(q1, q2):
    while True:
        item = q1.get()
        if item is None:
            q2.put(None)  # pass stop signal along
            break
        transformed = {"id": item["id"], "value": item["value"] ** 2}
        q2.put(transformed)
        print(f"Processor squared value: {item} -> {transformed}")

def writer(q2, results):
    while True:
        item = q2.get()
        if item is None:
            break
        results.append(item)
        print(f"Writer saved item: {item}")

if __name__ == "__main__":
    q1 = queue.Queue()
    q2 = queue.Queue()
    final_results = []

    # Create threads
    t1 = threading.Thread(target=generator, args=(q1,))
    t2 = threading.Thread(target=processor, args=(q1, q2))
    t3 = threading.Thread(target=writer, args=(q2, final_results))

    # Start threads
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("\nFinal Results:", final_results)