import json
from unittest.mock import mock_open, patch


from src.external_api import read_financial_transactions_json as read_json



@patch("os.path.exists")
def test_read_json_success(mock_exists):
    mock_exists.return_value = True  # Мы обманули функцию, теперь она верит, что файл есть
    data = [{"id": 1}]
    with patch("builtins.open", mock_open(read_data=json.dumps(data))):
        assert read_json("test.json") == data

@patch("os.path.exists")
def test_read_json_empty(mock_exists):
    mock_exists.return_value = False
    assert read_json("none.json") == []
