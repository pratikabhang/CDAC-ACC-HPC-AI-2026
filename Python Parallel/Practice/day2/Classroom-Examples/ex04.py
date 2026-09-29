import threading
from vinutils import line


filename = None
cond = threading.Condition()

def printf(msg):
    print(f"[{threading.current_thread().name}] {msg}")

def inputf(msg):
    return input(f"[{threading.current_thread().name}] {msg}")

def write_fibo_series_to_file(limit:int)->None:
    global filename

    a, b = -1, 1
    fibo_nums = []
    for _ in range(limit):
        c = a + b
        fibo_nums.append(c)
        a, b = b, c

    with cond:
        if not filename:
            printf("waiting for the filename to be available...")
            cond.wait()
            # will only continue to execute the rest after some other
            # thread calls the cond.notify()
            printf("Got the filename now, continuing to save the series...")
            with open(filename, "wt") as file:
                file.write(",".join([str(n) for n in fibo_nums]))
            printf("Fibo series saved in {filename}")


def main():
    global cond, filename
    limit = int(inputf("Enter the number of fiboacci elements you want: "))
    t = threading.Thread(target=write_fibo_series_to_file, args=(limit,), name="fibo_thread")
    t.start()

    with cond:
        filename = inputf("Enter the filename to save: ")
        cond.notify()

    t.join()
    printf("End of main()")


if __name__ == "__main__":
    main()