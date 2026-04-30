import re
from collections import Counter


def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрует транзакции по статусу (EXECUTED, CANCELED и т.д.)"""
    return [item for item in data if item.get("state") == state]

def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует транзакции по дате"""
    return sorted(data, key=lambda x: x.get("date", ""), reverse=reverse)

def process_bank_search(data: list[dict], search_str: str) -> list[dict]:
    """Поиск транзакций по слову в описании с помощью регулярных выражений"""
    pattern = re.compile(search_str, re.IGNORECASE)
    return [
        transaction for transaction in data
        if transaction.get("description") and re.search(pattern, transaction["description"])
    ]

def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Подсчет количества операций в каждой категории"""
    descriptions = [transaction.get("description") for transaction in data]
    counts = Counter(descriptions)
    return {category: counts[category] for category in categories}