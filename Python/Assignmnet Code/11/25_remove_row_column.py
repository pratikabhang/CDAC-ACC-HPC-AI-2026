import pandas as pd

def remove_row_column():
    df = pd.DataFrame({"Name": ["A", "B", "C"], "Marks": [80, 90, 70], "City": ["Pune", "Mumbai", "Nashik"]})
    df = df.drop(index=1)
    return df.drop(columns=["City"])

print(remove_row_column())