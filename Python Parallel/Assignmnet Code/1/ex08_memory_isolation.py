import multiprocessing

shared_log = []

def log_message(msg):
    shared_log.append(msg)
    print(len(shared_log))

def fill_range(arr, start, end, value):
    for i in range(start, end):
        arr[i] = value

def compute_square(num, q):
    q.put((num, num ** 2))

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=log_message, args=("A",))
    p2 = multiprocessing.Process(target=log_message, args=("B",))
    p3 = multiprocessing.Process(target=log_message, args=("C",))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print(shared_log)

    arr = multiprocessing.Array('i', 10)
    p4 = multiprocessing.Process(target=fill_range, args=(arr, 0, 5, 1))
    p5 = multiprocessing.Process(target=fill_range, args=(arr, 5, 10, 2))
    p4.start()
    p5.start()
    p4.join()
    p5.join()
    print(list(arr))

    q = multiprocessing.Queue()
    workers = [multiprocessing.Process(target=compute_square, args=(i, q)) for i in range(4)]
    for w in workers:
        w.start()
    for w in workers:
        w.join()
    for _ in range(4):
        print(q.get())