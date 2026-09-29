import pandas as pd

def salary_statistics():
    df = pd.DataFrame({"Name": ["A", "B", "C"], "Salary": [40000, 55000, 70000]})
    return df["Salary"].max(), df["Salary"].min(), df["Salary"].mean()

maximum, minimum, average = salary_statistics()
print("Maximum:", maximum)
print("Minimum:", minimum)
print("Average:", average)