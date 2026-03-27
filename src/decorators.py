import functools
from typing import Any, Callable, Optional

def log(filename: Optional[str] = None) -> Callable:
    def wrapper(func: Callable) -> Callable:
        @functools.wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                write_log(message, filename)
                return result
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                write_log(message, filename)
                raise e
        return inner
    return wrapper

def write_log(message: str, filename: Optional[str]) -> None:
    if filename:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(message + "\n")
    else:
        print(message)