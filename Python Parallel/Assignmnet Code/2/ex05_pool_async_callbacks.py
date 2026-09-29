import multiprocessing
import time


completed_records = []


def process_record(record_id, data_chunk):
    time.sleep(0.5)

    return {
        "record_id": record_id,
        "processed_elements": len(data_chunk),
        "checksum": sum(data_chunk)
    }


def collect_result(result):
    completed_records.append(result)
    print("Completed:", result)


def log_error(error):
    print("Error:", error)


if __name__ == "__main__":
    pool = multiprocessing.Pool()

    for i in range(8):
        chunk = list(range(i + 1, i + 6))

        pool.apply_async(
            process_record,
            args=(i, chunk),
            callback=collect_result,
            error_callback=log_error
        )

    # Visual ticker: main process is still running.
    while len(completed_records) < 8:
        print(".", end="", flush=True)
        time.sleep(0.1)

    print()

    pool.close()
    pool.join()

    print("\nAll records processed.")
    print("Summary:")

    for result in completed_records:
        print(result)
