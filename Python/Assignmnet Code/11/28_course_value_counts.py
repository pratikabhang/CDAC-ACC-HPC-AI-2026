import pandas as pd

def count_courses():
    df = pd.DataFrame({"Name": ["A", "B", "C", "D", "E"], "Course": ["Python", "Java", "Python", "C++", "Python"]})
    return df["Course"].value_counts()

print(count_courses())