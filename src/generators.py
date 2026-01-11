def filter_by_currency(transactions, currency):
    """Фильтрует транзакции по валюте."""
    return (t for t in transactions if t.get("operationAmount", {}).get("currency", {}).get("code") == currency)

def transaction_descriptions(transactions):
    """Возвращает описания транзакций."""
    for t in transactions:
        yield t.get("description", "")

def card_number_generator(start, stop):
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX."""
    for num in range(start, stop + 1):
        s = f"{num:016}"
        yield f"{s[:4]} {s[4:8]} {s[8:12]} {s[12:16]}"