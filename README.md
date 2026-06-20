# Applied Analytics Mini Project — Vibe KPI Demo

Setup and run commands assume you have already activated your Python virtual environment.

Install requirements:

```bash
pip install -r requirements.txt
```

Build the SQLite DB from CSV (ETL):

```bash
python -m src.etl_load_sqlite
```

Run the KPI script (prints two calls):

```bash
python -m src.kpi_city
```

Run tests:

```bash
pytest -q
```
# First_Repo
Created my first repository for learning purpose
