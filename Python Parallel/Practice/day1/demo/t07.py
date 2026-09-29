from time import sleep
import threading
# import multiprocessing

words = []
lock = threading.Lock()

def split_sentence(sentence: str) -> None:
    data = sentence.split(" ")
    with lock:
        for d in data:
            words.append(d)
            sleep(.0025)

    # print("Words = ", words)


def main():
    t1 = threading.Thread(target=split_sentence, args=["my name is vinod and i am from bangalore"])
    t2 = threading.Thread(target=split_sentence, args=["the quick brown fox jumps over the lazy dog"])
    t3 = threading.Thread(target=split_sentence, args=["python has both multirhead and multiprocess capabilities"])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Wrods = ", words)


if __name__ == "__main__":
    main()
