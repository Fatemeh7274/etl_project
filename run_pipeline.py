import os

os.system("python extract/extract_orders.py")
os.system("python transform/transform_orders.py")
os.system("python load/load_to_postgres.py")
