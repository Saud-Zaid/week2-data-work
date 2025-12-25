import pandas as pd
from pathlib import Path
from bootcamp_data.config import make_paths
import sys

root = Path(__file__).resolve().parents[1]
#sys.path.append(str(root/'src'))
path = make_paths(root)

from bootcamp_data.transforms import *
from bootcamp_data.io import *
from bootcamp_data.quality import assert_in_range


def main() -> None:

    orders = read_parquet(path.processed / 'orders.parquet')
    
    users = read_parquet(path.processed / 'users.parquet')
    
    
    #print(missing_report(orders))
    #print(missing_report(users))
    
    
    orders = enforce_schema_orders(orders)
    users = enforce_schema_users(users)
    
    orders['status_clean'] = normalize_text(orders['status'])
    #orders['status_clean'] = orders['status'].apply(normalize_text)
    #orders['flags'] = add_missing_flags(orders, {"amount", "quantity"})
    flags_df = add_missing_flags(orders, {"amount", "quantity"})
    orders = pd.concat([orders, flags_df], axis=1)
    

    print(orders)
    
    orders = orders.loc[:, ~orders.columns.duplicated()]
    
    write_parquet(orders, path.processed / "orders_clean.parquet")
    
    #assert_in_range(order_status_clean["amount"], lo=0, name="amount")
    #assert_in_range(order_status_clean["quantity"], lo=0, name="quantity")

if __name__ == "__main__":
    main()