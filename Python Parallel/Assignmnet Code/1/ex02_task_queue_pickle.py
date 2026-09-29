import math
import pickle
import os

# 1. Define the ComputeTask class
class ComputeTask:
    def __init__(self, task_id, operation, input_value):
        self.task_id = task_id
        self.operation = operation
        self.input_value = input_value
        self.result = None

    def execute(self):
        if self.operation == "square":
            self.result = self.input_value ** 2
        elif self.operation == "cube":
            self.result = self.input_value ** 3
        elif self.operation == "factorial":
            self.result = math.factorial(self.input_value)

    def __repr__(self):
        return f"Task(id={self.task_id}, op='{self.operation}', value={self.input_value}, result={self.result})"

def main():
    filename = "task_queue.pkl"

    # 2. Create a list of 5 ComputeTask objects with different operations and values
    tasks = [
        ComputeTask(1, "square", 4),
        ComputeTask(2, "cube", 3),
        ComputeTask(3, "factorial", 5),
        ComputeTask(4, "square", 6),
        ComputeTask(5, "cube", 2)
    ]

    # 3. Execute only the first 2 tasks
    print("Executing the first 2 tasks...")
    tasks[0].execute()
    tasks[1].execute()

    # 4. Pickle the entire list to a file using binary write mode ("wb")
    print(f"Saving tasks to '{filename}' using pickle...")
    with open(filename, "wb") as f:
        pickle.dump(tasks, f)

    # 5. Unpickle the list from the file using binary read mode ("rb")
    print("Loading tasks back from the pickle file...\n")
    with open(filename, "rb") as f:
        loaded_tasks = pickle.load(f)

    print("--- State After Unpickling ---")
    for task in loaded_tasks:
        print(task)

    # 6. Execute the remaining tasks on the unpickled list
    print("\nExecuting the remaining tasks...")
    for task in loaded_tasks:
        if task.result is None:
            task.execute()

    print("\n--- Final State of All Tasks ---")
    for task in loaded_tasks:
        print(task)

    # Clean up temporary pickle file
    if os.path.exists(filename):
        os.remove(filename)
        print(f"\nCleaned up temporary file: {filename}")

if __name__ == "__main__":
    main()