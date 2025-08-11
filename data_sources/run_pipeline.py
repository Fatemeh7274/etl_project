import os
import datetime

def log_message(message):
    with open("etl_log.txt", "a", encoding="utf-8") as log:
        log.write(f"[{datetime.datetime.now()}] {message}\n")

log_message("ETL started")

# اجرای مرحله Extract
os.system("python extract/extract_orders.py")
log_message("Extract completed")

# اجرای مرحله Transform
os.system("python transform/transform_orders.py")
log_message("Transform completed")

# اجرای مرحله Load
os.system("python load/load_to_postgres.py")
log_message("Load completed")

log_message("ETL finished")
