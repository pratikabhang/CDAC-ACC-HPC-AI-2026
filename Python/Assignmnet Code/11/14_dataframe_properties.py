import pandas as pd

def dataframe_properties():
    return pd.DataFrame({"Name": ["A", "B", "C"], "Marks": [70, 80, 90]})

df = dataframe_properties()
print("Shape:", df.shape)
print("Columns:", list(df.columns))
print("Data types:", df.dtypes)
print("Size:", df.size)