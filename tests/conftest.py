import pytest


@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T12:00:00"},
        {"id": 2, "state": "CANCELED", "date": "2023-02-01T12:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-15T12:00:00"},
    ]
