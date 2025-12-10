# etl/load_database.py
import sqlite3
import pandas as pd

DB = "atlas.db"
CSV_FILE = "data/clean_transactions.csv"

def load_db():
    df = pd.read_csv(CSV_FILE)

    conn = sqlite3.connect(DB)
    df.to_sql("transactions", conn, if_exists="replace", index=False)
    conn.close()

    print(f"[LOAD] Datos cargados en la base SQLite '{DB}'")

if __name__ == "__main__":
    load_db()
