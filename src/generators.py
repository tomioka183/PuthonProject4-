from typing import Any, Iterable, Iterator


def filter_by_currency(transactions: Iterable[dict], currency: str) -> Iterator[dict]:
    """
    Фильтрует транзакции по заданной валюте.
    Возвращает итератор.
    """
    return (transaction for transaction in transactions
            if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency)


def transaction_descriptions(transactions: Iterable[dict]) -> Iterator[str]:
    """
    Генератор, который возвращает описание каждой операции по очереди.
    """
    for transaction in transactions:
        yield transaction.get("description", "Описание отсутствует")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров карт в формате XXXX XXXX XXXX XXXX.
    Принимает диапазон от start до stop.
    """
    for number in range(start, stop + 1):

        num_str = f"{number:016}"

        formatted_card = f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"
        yield formatted_card