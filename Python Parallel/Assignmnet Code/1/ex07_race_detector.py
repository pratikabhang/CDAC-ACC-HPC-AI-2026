import threading
import time

# Unsafe withdrawal (causes race condition bug)
def withdraw_unsafe(account):
    current = account["balance"]
    time.sleep(0.001)  # Simulates delay, exposing the bug
    account["balance"] = current - 1

# Safe withdrawal (protected by a Lock)
def withdraw_safe(account, lock):
    with lock:  # Only one thread can change the balance at a time
        current = account["balance"]
        time.sleep(0.001)
        account["balance"] = current - 1

if __name__ == "__main__":
    # 1. Unsafe Test
    account_1 = {"balance": 100}
    threads = [threading.Thread(target=withdraw_unsafe, args=(account_1,)) for _ in range(50)]
    for t in threads: t.start()
    for t in threads: t.join()
    print(f"Unsafe Final Balance (Expected 50): {account_1['balance']}")

    # 2. Safe Test with a Lock
    account_2 = {"balance": 100}
    lock = threading.Lock()
    threads = [threading.Thread(target=withdraw_safe, args=(account_2, lock)) for _ in range(50)]
    for t in threads: t.start()
    for t in threads: t.join()
    print(f"Safe Final Balance   (Expected 50): {account_2['balance']}")