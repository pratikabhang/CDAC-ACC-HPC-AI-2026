import pandas as pd

def sort_students():
    df = pd.DataFrame({"Name": ["A", "B", "C"], "Marks": [70, 90, 80]})
    return df.sort_values("Marks", ascending=False)

print(sort_students())