import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator

def test_filter_by_currency():
    data = [{"operationAmount": {"currency": {"code": "USD"}}}]
    gen = filter_by_currency(data, "USD")
    assert next(gen)["operationAmount"]["currency"]["code"] == "USD"

def test_transaction_descriptions():
    data = [{"description": "test"}]
    gen = transaction_descriptions(data)
    assert next(gen) == "test"

def test_card_number_generator():
    gen = card_number_generator(1, 1)
    assert next(gen) == "0000 0000 0000 0001"