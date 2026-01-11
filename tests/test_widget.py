import pytest
from src.widget import get_date, mask_account_card

@pytest.mark.parametrize("info, expected", [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("Maestro 1596837405948271", "Maestro 1596 83** **** 8271")
])
def test_mask_account_card(info, expected):
    assert mask_account_card(info) == expected

def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2018-07-11T02:26:18.671407") == "11.07.2018"