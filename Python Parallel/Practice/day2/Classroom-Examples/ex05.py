import threading
import time


def function1():
    while True:
        # simulation of some serious background activity
        # such as capturing memory, user cursor tracking, logs....
        print(".", end="", flush=True)
        time.sleep(.3)


def main():
    t1 = threading.Thread(target=function1)
    print(f"{t1.daemon = }")
    t1.daemon = True
    print(f"{t1.daemon = }")
    t1.start()

    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")
        time.sleep(.7)

    print("End of main()")

if __name__ == "__main__":
    main()