import pytest
from src.decorators import log

def test_log_console_success(capsys):
    @log()
    def my_func(x):
        return x
    my_func(10)
    captured = capsys.readouterr()
    assert captured.out.strip() == "my_func ok"

def test_log_console_error(capsys):
    @log()
    def my_error_func():
        return 1 / 0
    with pytest.raises(ZeroDivisionError):
        my_error_func()
    captured = capsys.readouterr()
    assert "my_error_func error: ZeroDivisionError" in captured.out

def test_log_file(tmp_path):
    log_file = tmp_path / "test.log"
    @log(filename=str(log_file))
    def my_func(x):
        return x
    my_func(5)
    with open(log_file) as f:
        assert f.read().strip() == "my_func ok"