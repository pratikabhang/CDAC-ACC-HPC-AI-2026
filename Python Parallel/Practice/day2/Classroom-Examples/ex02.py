import os
import threading
import time
from vinutils import line


def write_words_to_file(sentence, file):
    """
    Split the sentence into words and writes each word in to the file in separate lines.

    Args:
    sentence - input sentence to be split into words
    file - text file object open in append mode
    """
    for word in sentence.split(" "):
        file.write(word)
        file.write("\n")
        time.sleep(0.00000000000000000000000000001)

def main():
    sentences = [
        "my name is Vinod and i am from Bangalore",
        "today in CDAC we are learning more about threads in python",
        "quick brown fox jumps over lazy dog"
    ]

    all_threads = []
    with open("words.txt", "at") as f1:
        for sentence in sentences:
            t = threading.Thread(target=write_words_to_file, args=(sentence, f1))
            all_threads.append(t)
            t.start()
        # outside of `for` loop
        print(f"at this time there are {threading.active_count()} threads")
        # we should wait until all threads finish their job; 
        # only then we should exit the `with` block
        [t.join() for t in all_threads]

    # outside of `with` block; f1 is closed here and not accessible anymore
    print("All sentences are written to the file `words.txt`")

    
if __name__ == "__main__":
    os.remove("./words.txt")
    line()
    print(f"At the start, there are {threading.active_count()} threads")
    main()
    print(f"At the end there are {threading.active_count()} threads")
    line()