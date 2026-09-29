"""
Demo 01: Data Serialization with JSON
======================================

Demonstrates how to serialize (encode) and deserialize (decode) standard
Python data structures using the built-in `json` module.

Key concepts:
    - json.dumps()  → Python object  → JSON string
    - json.loads()  → JSON string    → Python object
    - json.dump()   → Python object  → JSON file
    - json.load()   → JSON file      → Python object

Why it matters for parallel programming:
    JSON is a lightweight, human-readable format commonly used
    for exchanging data between processes, services, and systems.
"""

import json
import os


# ---------------------------------------------------------------------------
# 1. Basic serialization: Python dict → JSON string
# ---------------------------------------------------------------------------

def demo_basic_serialization():
    """Serialize a Python dict into a JSON-formatted string and back."""
    student = {
        "name": "Alice",
        "age": 25,
        "courses": ("HPC", "Parallel Programming", "Python"),
        "graduated": False,
        "gpa": 8.75,
    }

    # Serialize (encode) the dict into a JSON-formatted string
    json_string = json.dumps(student, indent=4)
    print("1. Python dict → JSON string:")
    print(json_string)
    print()

    # Deserialize (decode) the JSON string back into a Python dict
    restored = json.loads(json_string)
    print("2. JSON string → Python dict:")
    print(f"   Name    : {restored['name']}")
    print(f"   Courses : {restored['courses']}")
    print(f"   Type    : {type(restored)}")
    print(f"   Original: {student}")
    print(f"   Restored: {restored}")


# ---------------------------------------------------------------------------
# 2. Serializing a list of records
# ---------------------------------------------------------------------------

def demo_list_serialization():
    """Serialize a list of dictionaries (records) to JSON."""
    records = [
        {"id": 1, "task": "matrix_multiply", "time_sec": 2.34},
        {"id": 2, "task": "sort_array",      "time_sec": 0.56},
        {"id": 3, "task": "fft_transform",   "time_sec": 1.12},
    ]

    json_list = json.dumps(records, indent=2)
    print("3. List of records as JSON:")
    print(json_list)


# ---------------------------------------------------------------------------
# 3. Writing JSON to a file and reading it back
# ---------------------------------------------------------------------------

def demo_file_io():
    """Write JSON to a file and read it back."""
    records = [
        {"id": 1, "task": "matrix_multiply", "time_sec": 2.34},
        {"id": 2, "task": "sort_array",      "time_sec": 0.56},
        {"id": 3, "task": "fft_transform",   "time_sec": 1.12},
    ]

    output_file = "benchmark_results.json"

    # Write to file
    with open(output_file, "w") as f:
        json.dump(records, f, indent=2)

    print(f"4. Written {len(records)} records to '{output_file}'")

    # Read from file
    with open(output_file, "r") as f:
        loaded_records = json.load(f)

    print(f"Read back {len(loaded_records)} records from file:")
    for rec in loaded_records:
        print(f"Task: {rec['task']:20s}  Time: {rec['time_sec']}s")

    # Clean up
    os.remove(output_file)
    print(f"(Cleaned up '{output_file}')")


# ---------------------------------------------------------------------------
# 4. JSON limitations: only standard types are supported
# ---------------------------------------------------------------------------

def demo_limitations():
    """Show what JSON can and cannot serialize."""
    print("5. JSON supports: str, int, float, bool, None, list, dict")
    print("   JSON does NOT support: set, tuple (converted to list),")
    print("   bytes, datetime, custom objects — use Pickle for those.")


# ---------------------------------------------------------------------------
# Main: uncomment functions one by one to demonstrate each concept
# ---------------------------------------------------------------------------

def main():
    demo_basic_serialization()
    # demo_list_serialization()
    # demo_file_io()
    # demo_limitations()


if __name__ == "__main__":
    main()
