import time
import os
import random
from scoop import futures as scoop_futures

def print1(msg):
    pid = os.getpid()
    print(f"[{pid:6}] {msg}")

def time_taking_task_simulation(data):
    print1(f"executing time taking function using data as {data}")
    time.sleep(random.randrange(2, 5))
    print1(f"completed executing time taking function for data {data}")
    return data ** 2

def main():
    workload = [12, 49, 59, 204, 2882, -483]
    print1(f"{workload = }")
    results = list(scoop_futures.map(time_taking_task_simulation, workload))
    print1(f"{results = }")

if __name__ == "__main__":
    main()

# run this script with the following command:
# python3 -m scoop example.py
# load will be distributed across multiple processes

# python3 -m scoop --hosts hosts.txt example.py
    # hosts.txt contains a list of ip addresses
    # load will be distributed across multiple nodes and processes
    
# If you run with out scoop
# python example.py
# all tasks will be executed in single process
