import pytest

from src.generators import (card_number_generator, filter_by_currency,
                        transaction_descriptions)

# Кусочек данных для теста
test_transactions = [
    {"operationAmount": {"currency": {"code": "USD"}}, "description": "Перевод 1"},
    {"operationAmount": {"currency": {"code": "RUB"}}, "description": "Перевод 2"},
]

def test_filter_by_currency():
    # Проверяем, что фильтр находит только USD
    result = list(filter_by_currency(test_transactions, "USD"))
    assert len(result) == 1
    assert result[0]["operationAmount"]["currency"]["code"] == "USD"

def test_transaction_descriptions():
    # Проверяем, что выдаются правильные описания
    descriptions = list(transaction_descriptions(test_transactions))
    assert descriptions == ["Перевод 1", "Перевод 2"]

def test_card_number_generator():
    # Проверяем генератор номеров
    generator = card_number_generator(1, 2)
    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"