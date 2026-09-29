import threading
from time import sleep


def do_something(name):
    for _ in range(10):
        print(name, end=" ", flush=True)
        sleep(.25)


def main():
    # do_something("Vinod")
    # do_something("Shyam")
    t1 = threading.Thread(target=do_something, args=["Vinod"])
    t2 = threading.Thread(target=do_something, args=["Shyam"])

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("End of main()")


if __name__ == "__main__":
    main()
    