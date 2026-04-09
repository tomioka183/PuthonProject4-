import json
import os
from typing import Any


def read_json(path: str) -> list[dict[str, Any]]:
    """Читает JSON-файл. Если файл пустой, не найден или не список — возвращает []"""
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, Exception):
        return []
