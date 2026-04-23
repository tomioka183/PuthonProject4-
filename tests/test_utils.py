from unittest.mock import MagicMock, patch

import pandas as pd
import pytest

from src.utils import read_financial_transactions_csv, read_financial_transactions_excel


@patch('os.path.exists')
@patch('pandas.read_csv')
def test_read_financial_transactions_csv(mock_read_csv, mock_exists):
    """Тест чтения CSV с имитацией существования файла"""
    mock_exists.return_value = True  # Притворяемся, что файл есть

    mock_data = [{'id': 1, 'amount': 100}, {'id': 2, 'amount': 200}]
    mock_read_csv.return_value = pd.DataFrame(mock_data)

    result = read_financial_transactions_csv('fake_path.csv')

    assert result == mock_data
    mock_read_csv.assert_called_once_with('fake_path.csv', delimiter=';')


@patch('os.path.exists')
@patch('pandas.read_excel')
def test_read_financial_transactions_excel(mock_read_excel, mock_exists):
    """Тест чтения Excel с имитацией существования файла"""
    mock_exists.return_value = True

    mock_data = [{'id': 3, 'amount': 500}]
    mock_read_excel.return_value = pd.DataFrame(mock_data)

    result = read_financial_transactions_excel('fake_path.xlsx')

    assert result == mock_data
    mock_read_excel.assert_called_once_with('fake_path.xlsx')


def test_read_files_not_found():
    """Тест когда файла действительно нет (без мока os.path.exists)"""
    assert read_financial_transactions_csv('non_existent.csv') == []
    assert read_financial_transactions_excel('non_existent.xlsx') == []
