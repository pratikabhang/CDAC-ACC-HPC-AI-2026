from vinutils import line
import threading
import time

def function1():
    for i in range(500):
        print(f"fuction1's loop - iteration #{i} in thread {threading.current_thread().name}")
        # time.sleep(0.1)
    print(f"end of the thread {threading.current_thread().name}")
    

def function2():
    for i in range(500):
        print(f"   fuction2's loop - iteration #{i} in thread {threading.current_thread().name}")
        # time.sleep(0.1)
    print(f"end of the thread {threading.current_thread().name}")
    

def main():
    print(f"inside the thread {threading.current_thread().name}")
    t1 = threading.Thread(target=function1)
    t2 = threading.Thread(target=function2)

    t1.start()
    t2.start()


if __name__ == "__main__":
    line()
    main()
    line()
    print(f"end of the thread {threading.current_thread().name}")
