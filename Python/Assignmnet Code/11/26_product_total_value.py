import pandas as pd

def calculate_total_value():
    df = pd.DataFrame({"Product": ["Laptop", "Mouse", "Keyboard"], "Price": [50000, 500, 1500], "Quantity": [2, 10, 5]})
    df["Total Value"] = df["Price"] * df["Quantity"]
    return df

print(calculate_total_value())