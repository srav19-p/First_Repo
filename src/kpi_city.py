import sqlite3
from typing import Dict, Any


def city_kpi(city: str, db_path: str = "data/db/analytics.db") -> Dict[str, Any]:
    conn = sqlite3.connect(db_path)
    try:
        cur = conn.cursor()
        cur.execute(
            "SELECT COUNT(*) as cnt, AVG(monthly_spend) as avg_spend, SUM(churned) as churned_sum FROM customers_raw WHERE city = ?",
            (city,)
        )
        row = cur.fetchone()
        result = {
            "city": city,
            "count": int(row[0]) if row[0] is not None else 0,
            "avg_monthly_spend": float(row[1]) if row[1] is not None else 0.0,
            "churned": int(row[2]) if row[2] is not None else 0,
        }
        return result
    finally:
        conn.close()


if __name__ == "__main__":
    # safe call
    print(city_kpi("Mumbai"))
    # injection attempt should NOT return all rows
    print(city_kpi("Mumbai' OR 1=1 --"))
