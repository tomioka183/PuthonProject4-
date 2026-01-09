from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(sample_data):
    result = filter_by_state(sample_data, "EXECUTED")
    assert len(result) == 2
    assert result[0]["id"] == 1


def test_sort_by_date(sample_data):
    result = sort_by_date(sample_data)
    assert result[0]["id"] == 2
