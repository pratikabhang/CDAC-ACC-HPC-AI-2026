import pandas as pd

def create_dataframe():
    data = {"Name": ["A", "B", "C", "D", "E", "F"], "Department": ["IT", "HR", "Sales", "IT", "HR", "Sales"], "Salary": [50000, 45000, 55000, 60000, 47000, 52000]}
    return pd.DataFrame(data)

df = create_dataframe()
print(df.head())