import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions)


@pytest.fixture
def sample_transactions():
    """Фикстура с тестовыми данными транзакций."""
    return [
        {"id": 1, "description": "Перевод организации", "operationAmount": {"currency": {"code": "RUB"}}},
        {"id": 2, "description": "Перевод со счета на счет", "operationAmount": {"currency": {"code": "USD"}}},
        {"id": 3, "description": "Перевод с карты на карту", "operationAmount": {"currency": {"code": "RUB"}}},
    ]


def test_filter_by_currency(sample_transactions):
    """Тест фильтрации по валюте."""
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    result = next(usd_transactions)
    assert result["id"] == 2
    with pytest.raises(StopIteration):
        next(usd_transactions)


def test_transaction_descriptions(sample_transactions):
    """Тест генератора описаний."""
    descriptions = transaction_descriptions(sample_transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"


@pytest.mark.parametrize("start, stop, expected", [
    (1, 2, ["0000 0000 0000 0001", "0000 0000 0000 0002"]),
    (9999, 10000, ["0000 0000 0000 9999", "0000 0000 0001 0000"]),
])
def test_card_number_generator(start, stop, expected):
    """Параметризованный тест генератора номеров карт."""
    gen = card_number_generator(start, stop)
    assert list(gen) == expected

    import pytest

    from generators import (card_number_generator, filter_by_currency,
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