import pandas as pd
import os

def categorize_amount(amount):
    if amount < 100:
        return "Low"
    elif amount < 500:
        return "Medium"
    else:
        return "High"

def transform_data():
    df = pd.read_csv("extract/extracted_orders.csv", parse_dates=["order_date"])

    df = df.dropna(subset=["order_id", "amount"])

    df["tax"] = df["amount"] * 0.09  # فرض ۹٪ مالیات

    df["amount_category"] = df["amount"].apply(categorize_amount)

    df["order_date"] = pd.to_datetime(df["order_date"])

    os.makedirs("transform", exist_ok=True)
    df.to_csv("transform/transformed_orders.csv", index=False)
    print("✅ Data transformed and saved.")

if __name__ == "__main__":
    transform_data()



