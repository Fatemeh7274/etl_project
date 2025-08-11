import pandas as pd
from sqlalchemy import create_engine, text
import os

def load_to_postgres():
    engine = create_engine(
        "postgresql+psycopg2://postgres:Fatemeh123@localhost:5432/data_engineer_project_utf8"
    )

    # خواندن داده تبدیل شده
    df = pd.read_csv("transform/transformed_orders.csv", parse_dates=["order_date"])

    # گرفتن آخرین تاریخ در جدول orders
    with engine.connect() as conn:
        result = conn.execute(text("SELECT MAX(order_date) FROM datawarehouse.orders"))
        last_date = result.scalar()

    if last_date is None:
        # اگر جدول خالیه کل داده‌ها رو وارد کن
        new_data = df
    else:
        # فقط داده‌های جدیدتر از آخرین تاریخ
        new_data = df[df["order_date"] > last_date]

    if not new_data.empty:
        new_data.to_sql(
            name="orders",
            con=engine,
            schema="datawarehouse",
            if_exists="append",
            index=False,
            method='multi'
        )
        print(f"✅ {len(new_data)} rows loaded to database.")
    else:
        print("⚠️ No new data to load.")

if __name__ == "__main__":
    load_to_postgres()
