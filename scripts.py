# extract_api.py

import requests
import pandas as pd
import os

def extract_data():
    url = "http://127.0.0.1:5000/orders"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)

        # ساخت پوشه در صورت نیاز
        os.makedirs("extract", exist_ok=True)

        output_path = os.path.join("extract", "extracted_orders.csv")
        df.to_csv(output_path, index=False)
        print(f"✅ Data saved to {output_path}")
        return df
    else:
        print("❌ Failed to fetch data:", response.status_code)
        return None

if __name__ == "__main__":
    extract_data()


