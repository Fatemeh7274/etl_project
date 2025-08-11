import pandas as pd
import os

def test_extracted_file_exists():
    assert os.path.exists("extract/extracted_orders.csv")

def test_transformed_file_columns():
    df = pd.read_csv("transform/transformed_orders.csv")
    expected_cols = ["order_id", "customer_name", "amount", "tax", "amount_category", "order_date"]
    assert all(col in df.columns for col in expected_cols)

def test_no_negative_amounts():
    df = pd.read_csv("transform/transformed_orders.csv")
    assert (df["amount"] >= 0).all()
