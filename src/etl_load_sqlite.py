import os
import pandas as pd
import sqlite3


def load_csv_to_sqlite(csv_path: str = "data/raw/customers_raw.csv", db_path: str = "data/db/analytics.db"):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    df = pd.read_csv(csv_path)
    conn = sqlite3.connect(db_path)
    try:
        df.to_sql("customers_raw", conn, if_exists="replace", index=False)
    finally:
        conn.close()


if __name__ == "__main__":
    load_csv_to_sqlite()
