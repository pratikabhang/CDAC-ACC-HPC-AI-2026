from celery_tasks import add, multiply
from celery.exceptions import TimeoutError
import os

def main():
    print(f"[{os.getpid():5}] Submitting tasks to the RobbitMQ broker...")
    # locally executed
    # r1 = add(10, 20)
    # r2 = multiply(10, 20)
    # print(f"[{os.getpid():5}] {r1=}, {r2=}")

    # submitted as tasks to celery via RabbitMQ
    r1 = add.delay(10, 20)
    r2 = multiply.delay(10, 20)
    print(f"[{os.getpid():5}] {r1.id=}, {r2.id=}")

    try:
        print(f"{r1.get(timeout=5) = }")     # blocks until the reuslt is ready
        print(f"{r2.get(timeout=5) = }")
    except TimeoutError as e:
        print("Timedout!!! -", e)

if __name__ == "__main__":
    main()
