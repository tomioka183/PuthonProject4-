# Финальная версия для проверки
def filter_by_currency(transactions, currency_code):
    """
    Фильтрует транзакции по коду валюты (например, 'USD').
    """
    for transaction in transactions:
        # Заходим вглубь словаря: сумма -> валюта -> код
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency_code:
            yield transaction

def transaction_descriptions(transactions):
    """
    Возвращает описание каждой операции по очереди.
    """
    for transaction in transactions:
        # Берем значение по ключу 'description'
        yield transaction.get("description", "Описание отсутствует")

def card_number_generator(start, stop):
    """
    Генерирует номера карт в формате XXXX XXXX XXXX XXXX в заданном диапазоне.
    """
    for number in range(start, stop + 1):
        # Превращаем число в строку и дополняем нулями до 16 знаков
        str_number = str(number).zfill(16)

        # Режем строку на части по 4 цифры и соединяем пробелами
        formatted_number = f"{str_number[:4]} {str_number[4:8]} {str_number[8:12]} {str_number[12:]}"
        yield formatted_number