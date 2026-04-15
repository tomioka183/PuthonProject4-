import logging
import os

import requests
from dotenv import load_dotenv

logger = logging.getLogger('external_api')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('logs/external_api.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

# Подгружаем секретный ключ из файла .env
load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert_to_rub(transaction: dict) -> float:
    """
    Конвертирует валюту транзакции в рубли, логируя процесс.
    """

    logger.debug(f"Начало конвертации для транзакции: {transaction.get('id', 'без ID')}")
    amount = float(transaction.get("operationAmount", {}).get("amount", 0))
    # Достаем код валюты
    currency = transaction.get("operationAmount", {}).get("currency", {}).get("code", "RUB")

    # Если уже рубли — конвертация не нужна
    if currency == "RUB":
        logger.info(f"Транзакция {transaction.get('id', 'без ID')} уже в RUB. Сумма: {amount}")
        return amount

    logger.debug(f"Запрос к API для конвертации {amount} {currency} в RUB")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"
    headers = {"apikey": API_KEY}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        data = response.json()
        result = float(data.get("result", 0.0))

        logger.info(f"Конвертация {amount} {currency} в RUB успешна. Результат: {result}")
        return result
    except requests.exceptions.RequestException as e:

        logger.error(f"Ошибка при запросе к API для {currency}: {e}")
        return 0.0
    except Exception as e:

        logger.error(f"Неизвестная ошибка при конвертации {currency}: {e}")
        return 0.0
