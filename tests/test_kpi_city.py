import os
import sys

# ensure project root is on sys.path so `src` package is importable during pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import etl_load_sqlite, kpi_city


def setup_module(module):
    # ensure DB is created from sample CSV
    etl_load_sqlite.load_csv_to_sqlite()


def test_city_kpi_happy_path():
    res = kpi_city.city_kpi("Mumbai")
    assert res["city"] == "Mumbai"
    assert res["count"] == 3
    assert res["avg_monthly_spend"] > 0


def test_city_kpi_injection_attempt():
    res = kpi_city.city_kpi("Mumbai' OR 1=1 --")
    # injection string should match no city
    assert res["count"] == 0
