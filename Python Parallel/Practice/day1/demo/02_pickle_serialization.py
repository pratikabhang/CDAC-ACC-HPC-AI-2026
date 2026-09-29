"""
Demo 02: Object Serialization with Pickle
==========================================

Demonstrates how to serialize (pickle) and deserialize (unpickle) complex
Python objects — including custom classes — using the built-in `pickle` module.

Key concepts:
    - pickle.dumps()  → Python object  → bytes
    - pickle.loads()  → bytes          → Python object
    - pickle.dump()   → Python object  → binary file
    - pickle.load()   → binary file    → Python object

Why it matters for parallel programming:
    Python's `multiprocessing` module uses pickle internally to send
    objects between processes (via Pipes, Queues, and Pool).  Understanding
    pickle helps you know what can and cannot be passed across processes.
"""

import pickle
import os


# ---------------------------------------------------------------------------
# Helper class used by multiple demos — must be at module level for pickling
# ---------------------------------------------------------------------------

class Task:
    """Represents a computational task with timing information."""

    def __init__(self, name, duration):
        self.name = name
        self.duration = duration    # in seconds
        self.completed = False

    def run(self):
        """Mark the task as completed."""
        self.completed = True

    def __repr__(self):
        status = "done" if self.completed else "pending"
        return f"Task(name='{self.name}', duration={self.duration}s, {status})"


# ---------------------------------------------------------------------------
# 1. Pickling basic Python types
# ---------------------------------------------------------------------------

def demo_pickle_basic_types():
    """Pickle and unpickle a dict containing tuples, sets, and lists."""
    data = {
        "numbers": [1, 2, 3, 4, 5],
        "matrix": [[1, 0], [0, 1]],
        "label": "identity",
        "dimensions": (2, 2),           # tuples are preserved (unlike JSON)
        "tags": {"linear_algebra", "math"},  # sets are supported too
    }

    # Serialize to bytes
    pickled_bytes = pickle.dumps(data)
    print("1. Pickle basic types:")
    print(f"   Original type : {type(data)}")
    print(f"   Pickled type  : {type(pickled_bytes)}")
    print(f"   Pickled bytes : {pickled_bytes}")
    print(f"   Pickled size  : {len(pickled_bytes)} bytes")
    print()

    # Deserialize back
    restored = pickle.loads(pickled_bytes)
    print(f"   Restored type : {type(restored)}")
    print(f"   Dimensions    : {restored['dimensions']} (type: {type(restored['dimensions']).__name__})")
    print(f"   Tags          : {restored['tags']} (type: {type(restored['tags']).__name__})")


# ---------------------------------------------------------------------------
# 2. Pickling custom objects
# ---------------------------------------------------------------------------

def demo_pickle_custom_objects():
    """Pickle a custom class instance and verify it retains its state."""
    task = Task("matrix_multiply", 3.5)
    task.run()  # mark it as completed

    print("2. Pickle custom objects:")
    print(f"   Original : {task}")

    # Serialize the custom object
    task_bytes = pickle.dumps(task)
    print(f"   Pickled  : {len(task_bytes)} bytes")

    # Deserialize — the object retains its class, attributes, and state
    restored_task = pickle.loads(task_bytes)
    print(f"   Restored : {restored_task}")
    print(f"   Same class? {type(restored_task).__name__} == Task → {isinstance(restored_task, Task)}")


# ---------------------------------------------------------------------------
# 3. Pickling to and from a file
# ---------------------------------------------------------------------------

def demo_pickle_file_io():
    """Write pickled objects to a binary file and read them back."""
    tasks = [
        Task("sort_array", 1.2),
        Task("fft_transform", 2.8),
        Task("eigenvalue", 5.0),
    ]

    output_file = "tasks.pkl"

    # Write to binary file
    with open(output_file, "wb") as f:
        pickle.dump(tasks, f)
    print(f"3. Written {len(tasks)} Task objects to '{output_file}'")

    # Read from binary file
    with open(output_file, "rb") as f:
        loaded_tasks = pickle.load(f)

    print(f"   Loaded {len(loaded_tasks)} Task objects:")
    for t in loaded_tasks:
        print(f"     {t}")

    # Clean up
    os.remove(output_file)
    print(f"   (Cleaned up '{output_file}')")


# ---------------------------------------------------------------------------
# 4. Pickle vs JSON — quick comparison
# ---------------------------------------------------------------------------

def demo_pickle_vs_json():
    """Print a comparison table of Pickle vs JSON."""
    print("4. Pickle vs JSON comparison:")
    print("   ┌────────────────┬──────────────┬──────────────┐")
    print("   │ Feature        │ JSON         │ Pickle       │")
    print("   ├────────────────┼──────────────┼──────────────┤")
    print("   │ Format         │ Text (UTF-8) │ Binary       │")
    print("   │ Human-readable │ Yes          │ No           │")
    print("   │ Custom objects  │ No           │ Yes          │")
    print("   │ Tuples / Sets  │ No           │ Yes          │")
    print("   │ Cross-language │ Yes          │ Python only  │")
    print("   │ Security       │ Safe         │ Unsafe*      │")
    print("   └────────────────┴──────────────┴──────────────┘")
    print("   * Never unpickle data from untrusted sources!")


# ---------------------------------------------------------------------------
# Main: uncomment functions one by one to demonstrate each concept
# ---------------------------------------------------------------------------

def main():
    # demo_pickle_basic_types()
    demo_pickle_custom_objects()
    # demo_pickle_file_io()
    # demo_pickle_vs_json()


if __name__ == "__main__":
    main()
