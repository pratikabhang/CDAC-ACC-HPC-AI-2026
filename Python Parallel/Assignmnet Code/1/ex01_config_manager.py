import json

# 1. Create the dictionary
config = {
    "job_name": "matrix_benchmark",
    "num_workers": 4,
    "chunk_size": 1000,
    "timeout_sec": 30.0,
    "retry_on_failure": True,
    "input_files": ["data_part1.csv", "data_part2.csv", "data_part3.csv"],
    "output_dir": "/results/run_001",
    "parameters": {
        "algorithm": "strassen",
        "precision": "double"
    }
}

# 2. Save it to a file called job_config.json
with open("job_config.json", "w") as f:
    json.dump(config, f, indent=4)

# 3. Read the file back
with open("job_config.json", "r") as f:
    loaded_config = json.load(f)

# 4. Change num_workers to 8 and save it again
loaded_config["num_workers"] = 8
with open("job_config.json", "w") as f:
    json.dump(loaded_config, f, indent=4)

# 5. Read it one final time and print it nicely
with open("job_config.json", "r") as f:
    final_config = json.load(f)
    print(json.dumps(final_config, indent=4))