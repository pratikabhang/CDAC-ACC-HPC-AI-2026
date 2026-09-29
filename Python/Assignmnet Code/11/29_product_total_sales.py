import pandas as pd

def total_sales():
    df = pd.DataFrame({"Product": ["A", "B", "A", "B"], "Sales": [100, 200, 150, 250]})
    return df.groupby("Product")["Sales"].sum()

print(total_sales())