import logging
import os
import json
import os
from typing import Any

os.makedirs('logs', exist_ok=True)

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)


file_handler = logging.FileHandler('logs/utils.log', mode='w', encoding='utf-8')


file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)


logger.addHandler(file_handler)





def read_json(path: str) -> list[dict[str, Any]]:
    if not os.path.exists(path):
        logger.error(f"Файл не найден по пути: {path}")
        return []

    try:
            data = json.load(f)
        return []
