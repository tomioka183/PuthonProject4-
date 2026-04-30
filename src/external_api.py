import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def convert_to_rub(transaction: dict) -> float:
    """Извлекает сумму транзакции и переводит в рубли, если она в USD или EUR."""
    amount = float(transaction.get('operationAmount', {}).get('amount', 0))
    currency = transaction.get('operationAmount', {}).get('currency', {}).get('code', 'RUB')

    if currency == 'RUB':
        return amount

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": API_KEY}

    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return float(data.get('result', 0.0))
        else:
            rates = {'USD': 90.0, 'EUR': 100.0}
            return amount * rates.get(currency, 1.0)
    except Exception:
        return 0.0

def read_financial_transactions_json(file_path):
    """Считывает данные из JSON-файла."""
    if not os.path.exists(file_path):
        return []
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, Exception):
        return []
