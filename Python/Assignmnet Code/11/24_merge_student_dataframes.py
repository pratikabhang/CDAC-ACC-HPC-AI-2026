import pandas as pd

def merge_dataframes():
    first = pd.DataFrame({"ID": [1, 2, 3], "Name": ["A", "B", "C"]})
    second = pd.DataFrame({"ID": [1, 2, 3], "Marks": [80, 90, 75]})
    return pd.merge(first, second, on="ID")

print(merge_dataframes())