from flask import Flask, jsonify
import uuid       # یونیک باشه  
import random     # به صورت تصادفی باشه 
import datetime   # تاریخ امروز 

app = Flask(__name__)  # ساخت برنامه‌ی Flask

@app.route("/orders")  # تعریف آدرس /orders
def get_orders():      # تابع رو اینطور تعریف میکنیم 
    return jsonify([
        {
            "order_id": str(uuid.uuid4()),
            "customer_name": f"Customer {i}",
            "amount": round(random.uniform(10, 1000), 2),
            "order_date": str(datetime.date.today())
        } for i in range(10)
    ])

if __name__ == "__main__":
    app.run(deb)

