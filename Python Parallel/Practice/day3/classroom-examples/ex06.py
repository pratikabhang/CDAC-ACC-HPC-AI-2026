from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from threading import current_thread
from multiprocessing import current_process
from time import sleep


def factorial(num):
    print(f"[{current_process().pid}] [{current_thread().name}] inside the factorial function, num = {num}")
    f = 1
    for i in range(1, num+1):
        f *= i
        print(f"[{current_process().pid}] [{current_thread().name}] factorial is under calcualtion (i={i}, f={f})")
        sleep(.1)

    print(f"[{current_process().pid}] [{current_thread().name}] got the result of {num}! as {f}")
    return f


def main():
    print(f"[{current_process().pid}] [{current_thread().name}] inside the main()")
    inputs = [4, 9, 10, 20]
    with ProcessPoolExecutor(max_workers=3) as executor:
    # with ThreadPoolExecutor(max_workers=3) as executor:
        future = executor.map(factorial, inputs)
        print(f"[{current_process().pid}] [{current_thread().name}] trying to kill time")
        for i in range(10):
            print(f"[{current_process().pid}] [{current_thread().name}] i = {i}")
            sleep(.1)

        for result in future:
            print(f"[{current_process().pid}] [{current_thread().name}] result = {result}")

if __name__ == "__main__":
    main()
