from pathlib import Path
root = Path(__file__).resolve().parents[1]

import sys

sys.path.append(str(root/'src'))

from bootcamp_data.config import make_paths
from bootcamp_data.io import * 
from bootcamp_data.transforms import * 

path = make_paths(root)

print(path)

users = read_users_csv(path.raw / "users.csv")
orders = read_orders_csv(path.raw / "orders.csv")

print(users)

schema_orders = enforce_schema_orders(orders)
schema_users = enforce_schema_users(users)

write_parquet(schema_orders, path.processed / "orders.parquet" )
write_parquet(schema_users, path.processed / "users.parquet" )