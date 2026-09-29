import multiprocessing
import time
import os

def function1(msg):
    for i in range(1500):
        print(
            f"{i+1}. Message from process {multiprocessing.current_process().name} "
            f" [PID: {os.getpid()}]"
            f" - {msg}"
        )
        time.sleep(.3)


def main():

    t1 = multiprocessing.Process(target=function1, args=("Welcome",), name="t1")
    t1.start()

    msg = "Hello"
    for i in range(1500):
        print(
            f"{i+1}. Message from process {multiprocessing.current_process().name} "
            f" [PID: {os.getpid()}]"
            f" - {msg}"
        )
        time.sleep(.3)

if __name__ == "__main__":
    main()
