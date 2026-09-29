import pandas as pd

def average_salary_by_department():
    df = pd.DataFrame({"Name": ["A", "B", "C", "D"], "Department": ["IT", "HR", "IT", "HR"], "Salary": [60000, 50000, 70000, 55000]})
    return df.groupby("Department")["Salary"].mean()

print(average_salary_by_department())