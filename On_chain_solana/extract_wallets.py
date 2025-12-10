# etl/extract_wallets.py
import requests
import json
import os

HELIUS_API_KEY = os.getenv("HELIUS_API_KEY")
WALLET = os.getenv("TARGET_WALLET")  # La wallet que quieres analizar
OUTPUT_FILE = "data/raw_wallet.json"

def extract_wallet_data():
    url = f"https://mainnet.helius-rpc.com/?api-key={HELIUS_API_KEY}"

    payload = {
        "jsonrpc": "2.0",
        "id": "extract",
        "method": "getSignaturesForAddress",
        "params": [WALLET, {"limit": 100}]
    }

    response = requests.post(url, json=payload)
    data = response.json()

    os.makedirs("data", exist_ok=True)
    with open(OUTPUT_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print(f"[EXTRACT] Datos crudos guardados en {OUTPUT_FILE}")

if __name__ == "__main__":
    extract_wallet_data()
