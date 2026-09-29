import pandas as pd

def fill_missing_values():
    df = pd.DataFrame({"Name": ["A", "B", "C"], "Marks": [80, None, 90]})
    return df.fillna({"Marks": 0})

print(fill_missing_values())