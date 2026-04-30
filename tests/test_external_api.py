from unittest.mock import patch

from src.external_api import convert_to_rub


@patch("requests.get")
def test_convert_usd(mock_get):
    mock_get.return_value.json.return_value = {"result": 9000.0}
    mock_get.return_value.status_code = 200

    transaction = {
        "operationAmount": {"amount": "100", "currency": {"code": "USD"}}
    }
    assert convert_to_rub(transaction) == 9000.0


def test_convert_rub():
    transaction = {
        "operationAmount": {"amount": "500", "currency": {"code": "RUB"}}
    }
    assert convert_to_rub(transaction) == 500.0
