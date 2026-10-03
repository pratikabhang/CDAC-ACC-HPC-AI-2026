import time
import os
from celery_app import app

@app.task
def add(a, b):
    pid = os.getpid()
    print(f"[{pid:6}] Adding {a} and {b}...")
    # simulate complex time-taking task
    time.sleep(3)
    result = a + b
    print(f"[{pid:6}] Result of adding {a} and {b} is {result}")
    return result


@app.task
def multiply(a, b):
    pid = os.getpid()
    print(f"[{pid:6}] Multiplying {a} and {b}...")
    time.sleep(15)
    result = a * b
    print(f"[{pid:6}] Result of multiplying {a} and {b} is {result}")
    return result

