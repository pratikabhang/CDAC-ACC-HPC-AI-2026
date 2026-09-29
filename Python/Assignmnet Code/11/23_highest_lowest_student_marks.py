import pandas as pd

def highest_lowest_student():
    df = pd.DataFrame({"Name": ["A", "B", "C"], "Marks": [75, 95, 60]})
    return df.loc[df["Marks"].idxmax()], df.loc[df["Marks"].idxmin()]

highest, lowest = highest_lowest_student()
print("Highest:")
print(highest)
print("Lowest:")
print(lowest)