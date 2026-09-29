import multiprocessing
import time

cpn = lambda :multiprocessing.current_process().name 

def is_prime(num):
    half = num//2
    for i in range(2, half+2):
        if num % i == 0:
            return False
    return True


def find_prime_between(q:multiprocessing.Queue, start:int, end:int):
    for i in range(start, end+1):
        if is_prime(i):
            print(f"[{cpn()}] stored {i} in the queue")
            q.put(i)            # value of `i` is serialized using pickle
            time.sleep(.02)


def process_prime_numbers(q:multiprocessing.Queue):
    while True:
        n = q.get()             # value in the queue is deserialized using pickle
        print(f"\t[{cpn()}] Got {n} from the queue")

def main():
    q = multiprocessing.Queue()     # shared placeholder for two processes
                                    # managed by python runtime

    p1 = multiprocessing.Process(
        target=find_prime_between, 
        args=(q, 1, 100), 
        name="find_prime_between"
    )
    p2 = multiprocessing.Process(
        target=process_prime_numbers, 
        args=(q,), 
        name="process_prime_numbers",
        daemon=True
    )
    p1.start()
    p2.start()

    p1.join()
    print(f"[{cpn()}] End of main()")


if __name__ == "__main__":
    main()