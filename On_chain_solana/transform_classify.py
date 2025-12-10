# etl/transform_classify.py
import json
import os
import pandas as pd

RAW_FILE = "data/raw_wallet.json"
TRANSFORMED_FILE = "data/clean_transactions.csv"

def classify_tx(sig):
    if "swap" in sig.lower():
        return "swap"
    if "stake" in sig.lower():
        return "stake"
    if "transfer" in sig.lower():
        return "transfer"
    return "unknown"

def transform_data():
    with open(RAW_FILE, "r") as f:
        raw = json.load(f)

    signatures = raw.get("result", [])

    rows = []
    for item in signatures:
        rows.append({
            "signature": item["signature"],
            "slot": item.get("slot"),
            "err": item.get("err"),
            "blockTime": item.get("blockTime"),
            "classification": classify_tx(item["signature"])
        })

    df = pd.DataFrame(rows)
    df.to_csv(TRANSFORMED_FILE, index=False)

    print(f"[TRANSFORM] Datos limpios guardados en {TRANSFORMED_FILE}")

if __name__ == "__main__":
    transform_data()
