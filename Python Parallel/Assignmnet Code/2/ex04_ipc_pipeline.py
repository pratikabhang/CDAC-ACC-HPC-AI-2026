import multiprocessing
import random


# Producer process
def producer(queue):
    for _ in range(15):
        number = random.randint(1, 100)

        queue.put(number)

        print("[Producer] Sent:", number)

    # Sentinel value
    queue.put(None)


# Filter process
def filter_numbers(queue, pipe_connection):
    while True:
        number = queue.get()

        # Stop when producer is finished
        if number is None:
            pipe_connection.send(None)
            break

        # Keep only even numbers
        if number % 2 == 0:
            pipe_connection.send(number)
            print("[Filter] Sent even number:", number)

    pipe_connection.close()


# Writer process
def writer(pipe_connection):
    values = []

    while True:
        number = pipe_connection.recv()

        # Stop when filter is finished
        if number is None:
            break

        values.append(number)

        print("[Writer] Accepted:", number)

    print("[Writer] Final values:", values)

    pipe_connection.close()


if __name__ == "__main__":

    # Create Queue
    queue = multiprocessing.Queue()

    # Create Pipe
    filter_connection, writer_connection = multiprocessing.Pipe()

    # Create Producer process
    producer_process = multiprocessing.Process(
        target=producer,
        args=(queue,)
    )

    # Create Filter process
    filter_process = multiprocessing.Process(
        target=filter_numbers,
        args=(queue, filter_connection)
    )

    # Create Writer process
    writer_process = multiprocessing.Process(
        target=writer,
        args=(writer_connection,)
    )

    # Start all processes
    producer_process.start()
    filter_process.start()
    writer_process.start()

    # Wait for all processes
    producer_process.join()
    filter_process.join()
    writer_process.join()

    print("Pipeline finished.")