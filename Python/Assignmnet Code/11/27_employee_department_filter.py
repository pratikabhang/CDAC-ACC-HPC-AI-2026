import pandas as pd

def filter_department():
    df = pd.DataFrame({"Name": ["A", "B", "C"], "Department": ["IT", "HR", "IT"]})
    return df[df["Department"] == "IT"]

print(filter_department())