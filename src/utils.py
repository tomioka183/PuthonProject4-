import os
import re
from collections import Counter
from typing import Dict, List

import pandas as pd


def read_financial_transactions_csv(file_path: str) -> List[Dict]:
    """Считывает CSV файл."""
    if not os.path.exists(file_path):
        return []
    try:
        df = pd.read_csv(file_path, delimiter=';')
        return df.to_dict(orient='records')
    except Exception:
        return []

def read_financial_transactions_excel(file_path: str) -> List[Dict]:
    """Считывает Excel файл."""
    if not os.path.exists(file_path):
        return []
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient='records')
    except Exception:
        return []

def search_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """Ищет транзакции по описанию через регулярные выражения."""
    result = []
    pattern = re.compile(search_string, re.IGNORECASE)
    for transaction in transactions:
        description = transaction.get("description", "")
        if pattern.search(description):
            result.append(transaction)
    return result

def count_transactions_by_category(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает количество операций в каждой категории."""
    descriptions = [t.get("description", "") for t in transactions]
    counts = Counter(descriptions)
    return {category: counts[category] for category in categories}