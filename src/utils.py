import pandas as pd
import os
from typing import List, Dict


def read_financial_transactions_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла и возвращает список словарей.
    Если файл не найден или произошла ошибка, возвращает пустой список.
    """
    if not os.path.exists(file_path):
        return []

    try:
        df = pd.read_csv(file_path, delimiter=';')

        if df.empty:
            return []

        return df.to_dict(orient='records')
    except Exception:
        return []


def read_financial_transactions_excel(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла (.xlsx) и возвращает список словарей.
    """
    if not os.path.exists(file_path):
        return []

    try:
        df = pd.read_excel(file_path)

        if df.empty:
            return []

        return df.to_dict(orient='records')
    except Exception:
        return []