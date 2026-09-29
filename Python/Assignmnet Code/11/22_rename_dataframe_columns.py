import pandas as pd

def rename_columns():
    df = pd.DataFrame({"student_name": ["A", "B"], "student_marks": [80, 90]})
    return df.rename(columns={"student_name": "Name", "student_marks": "Marks"})

print(rename_columns())