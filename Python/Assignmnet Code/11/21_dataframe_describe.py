import pandas as pd

def create_dataframe():
    return pd.DataFrame({"Marks": [65, 70, 80, 90, 75]})

df = create_dataframe()
print(df.describe())