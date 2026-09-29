import json
import pickle
import time
import multiprocessing
import os

def create_task_file():
    tasks = [
        {"id": 1, "operation": "sum_of_squares", "n": 2000000},
        {"id": 2, "operation": "sum_of_squares", "n": 3000000},
        {"id": 3, "operation": "sum_of_squares", "n": 1500000},
        {"id": 4, "operation": "sum_of_squares", "n": 2500000},
        {"id": 5, "operation": "sum_of_squares", "n": 1000000},
        {"id": 6, "operation": "sum_of_squares", "n": 3500000}
    ]
    with open("tasks.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)

def execute_task(task):
    start = time.time()
    result = sum(i * i for i in range(task["n"]))
    elapsed = time.time() - start
    return {
        "id": task["id"],
        "n": task["n"],
        "result": result,
        "time": round(elapsed, 4)
    }

if __name__ == "__main__":
    create_task_file()

    with open("tasks.json", "r", encoding="utf-8") as f:
        tasks = json.load(f)

    start_seq = time.time()
    seq_results = [execute_task(t) for t in tasks]
    total_seq_time = time.time() - start_seq

    start_par = time.time()
    with multiprocessing.Pool() as pool:
        par_results = pool.map(execute_task, tasks)
    total_par_time = time.time() - start_par

    with open("results.pkl", "wb") as f:
        pickle.dump(par_results, f)

    speedup = total_seq_time / total_par_time if total_par_time > 0 else 0
    num_workers = multiprocessing.cpu_count()
    efficiency = (speedup / num_workers) * 100

    print("Task ID | N         | Result              | Time (s)")
    print("-" * 55)
    for res in par_results:
        print(f"{res['id']:<7} | {res['n']:<9} | {res['result']:<19} | {res['time']}")

    print("-" * 55)
    print(f"Total Sequential Time: {total_seq_time:.4f} seconds")
    print(f"Total Parallel Time:   {total_par_time:.4f} seconds")
    print(f"Speedup:               {speedup:.2f}x")
    print(f"Efficiency:            {efficiency:.2f}%")

    if os.path.exists("tasks.json"):
        os.remove("tasks.json")
    if os.path.exists("results.pkl"):
        os.remove("results.pkl")