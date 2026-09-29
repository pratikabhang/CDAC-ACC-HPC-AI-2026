import json


def main():
    data = """[
  {
    "id": 1,
    "task": "matrix_multiply",
    "time_sec": 2.34
  },
  {
    "id": 2,
    "task": "sort_array",
    "time_sec": 0.56
  },
  {
    "id": 3,
    "task": "fft_transform",
    "time_sec": 1.12
  }
]"""
    print(f"{type(data) = }")
    data = json.loads(data)
    print(f"{type(data) = }")

    for d in data:
        print(f"{d["task"]} took {d["time_sec"]} seconds.")


if __name__ == "__main__":
    main()
