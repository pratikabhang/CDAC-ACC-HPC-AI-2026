import pandas as pd

def save_and_read():
    df = pd.DataFrame({"Name": ["A", "B", "C"], "Marks": [80, 90, 70]})
    df.to_csv("students.csv", index=False)
    return pd.read_csv("students.csv")

print(save_and_read())