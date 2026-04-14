import logging
import os
import json
from typing import Any

os.makedirs('logs', exist_ok=True)

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)


file_handler = logging.FileHandler('logs/utils.log', mode='w', encoding='utf-8')


file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)


logger.addHandler(file_handler)





def read_json(path: str) -> list[dict[str, Any]]:
    """
    Читает JSON-файл. Логирует попытку, успех и ошибки.
    Возвращает список транзакций или пустой список.
    """

    logger.debug(f"Попытка прочитать файл: {path}")

    if not os.path.exists(path):
        logger.error(f"Файл не найден по пути: {path}")
        return []

    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            logger.info(f"Файл {path} успешно прочитан. Найдено {len(data)} записей.")
            return data
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON в файле: {path}")
        return []
    except Exception as e:
        logger.error(f"Неизвестная ошибка при чтении файла {path}: {e}")
        return []