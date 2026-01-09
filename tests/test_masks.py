import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card, expected", [
    ("1234567812345678", "1234 56** **** 5678"),
    ("1111222233334444", "1111 22** **** 4444"),
    ("123", "Некорректный номер карты")
])
def test_mask_card(card, expected):
    assert get_mask_card_number(card) == expected


def test_mask_account():
    assert get_mask_account("73654108430135874305") == "**4305"
