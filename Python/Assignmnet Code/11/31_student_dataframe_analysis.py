import pandas as pd

def analyze_students():
    df = pd.DataFrame({"Name": ["A", "B", "C", "D"], "Course": ["Python", "Java", "Python", "Java"], "Marks": [80, 65, 90, 75]})
    filtered = df[df["Marks"] > 70]
    sorted_df = df.sort_values("Marks", ascending=False)
    grouped = df.groupby("Course")["Marks"].mean()
    statistics = df["Marks"].describe()
    return filtered, sorted_df, grouped, statistics

filtered, sorted_df, grouped, statistics = analyze_students()
print("Filtered:")
print(filtered)
print("Sorted:")
print(sorted_df)
print("Grouped:")
print(grouped)
print("Statistics:")
print(statistics)