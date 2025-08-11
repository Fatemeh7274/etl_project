from flask import Flask, jsonify
import random
import uuid
from datetime import date

app = Flask(__name__)

# جلوگیری از ارور favicon.ico
@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route("/orders", methods=["GET"])
def get_orders():
    orders = []

    for i in range(10):
        order = {
            "order_id": str(uuid.uuid4()),
            "customer_name": f"Customer {i}",
            "amount": round(random.uniform(10, 1000), 2),
            "order_date": str(date.today())
        }
        orders.append(order)

    return jsonify(orders)

if __name__ == "__main__":
    app.run(debug=True)



