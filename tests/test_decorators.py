import pytest
# Тест 1: Успешное выполнение функции и вывод в консоль
from src.decorators import log


def test_log_console_ok(capsys):
    @log()
    def test_func(x, y):
        return x + y

    test_func(1, 2)
    captured = capsys.readouterr()
    assert captured.out.strip() == "test_func ok"


# Тест 2: Ошибка в функции и вывод в консоль
def test_log_console_error(capsys):
    @log()
    def error_func():
        raise ValueError("Something went wrong")

    with pytest.raises(ValueError):
        error_func()

    captured = capsys.readouterr()
    # Проверяем, что в логе есть имя функции, тип ошибки и входные параметры
    assert "error_func error: ValueError. Inputs: (), {}" in captured.out


# Тест 3: Запись успешного результата в файл
def test_log_file_ok(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def test_func(x):
        return x

    test_func(5)

    with open(log_file, "r") as f:
        log_content = f.read().strip()
    assert log_content == "test_func ok"


# Тест 4: Запись ошибки в файл
def test_log_file_error(tmp_path):
    log_file = tmp_path / "test_error.log"

    @log(filename=str(log_file))
    def error_func(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        error_func(1, 0)

    with open(log_file, "r") as f:
         log_content = f.read().strip()
    assert "error_func error: ZeroDivisionError. Inputs: (1, 0), {}" in log_content