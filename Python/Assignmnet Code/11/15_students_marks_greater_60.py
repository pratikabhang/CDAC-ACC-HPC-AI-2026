import pandas as pd

def filter_students():
    df = pd.DataFrame({"Name": ["A", "B", "C", "D"], "Marks": [55, 72, 65, 48]})
    return df[df["Marks"] > 60]

print(filter_students())