import pytest
from src.utils import search_by_description, count_transactions_by_category

def test_search_by_description():
    data = [{"description": "Перевод организации"}, {"description": "Оплата услуг"}]
    assert len(search_by_description(data, "Перевод")) == 1
    assert len(search_by_description(data, "Кот")) == 0

def test_count_transactions_by_category():
    data = [{"description": "Перевод"}, {"description": "Перевод"}, {"description": "Оплата"}]
    categories = ["Перевод", "Оплата"]
    result = count_transactions_by_category(data, categories)
    assert result == {"Перевод": 2, "Оплата": 1}