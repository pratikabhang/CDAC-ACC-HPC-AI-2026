import pandas as pd

def create_dataframe():
    return pd.DataFrame({"Number": range(1, 11), "Value": range(10, 110, 10)})

df = create_dataframe()
print("First 5 records:")
print(df.head())
print("Last 5 records:")
print(df.tail())