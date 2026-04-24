from src.external_api import read_financial_transactions_json
from src.utils import (read_financial_transactions_csv,
                       read_financial_transactions_excel,
                       search_by_description)
from src.processing import filter_by_state, sort_by_date
from src.masks import get_mask_card_number, get_mask_account


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("Пользователь: ")

    if choice == '1':
        print("Для обработки выбран JSON-файл.")
        transactions = read_financial_transactions_json('data/operations.json')
    elif choice == '2':
        print("Для обработки выбран CSV-файл.")
        transactions = read_financial_transactions_csv('data/transactions.csv')
    elif choice == '3':
        print("Для обработки выбран XLSX-файл.")
        transactions = read_financial_transactions_excel('data/transactions_excel.xlsx')
    else:
        print("Неверный выбор.")
        return

    # Фильтрация по статусу
    status = input("\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
                   "Доступные статусы: EXECUTED, CANCELED, PENDING\n").upper()

    if status not in ['EXECUTED', 'CANCELED', 'PENDING']:
        print(f"Статус {status} недоступен. Вывожу все операции.")
    else:
        transactions = filter_by_state(transactions, status)
        print(f"Операции отфильтрованы по статусу {status}")

    # Сортировка по дате
    is_sort = input("Отсортировать операции по дате? Да/Нет: ").lower()
    if is_sort == 'да':
        is_asc = input("По возрастанию или по убыванию? ").lower()
        transactions = sort_by_date(transactions, is_asc == 'по возрастанию')

    # Фильтрация по RUB
    only_rub = input("Выводить только рублевые транзакции? Да/Нет: ").lower()
    if only_rub == 'да':
        transactions = [t for t in transactions if
                        t.get('operationAmount', {}).get('currency', {}).get('code') == 'RUB']

    # Поиск по описанию
    search_query = input("Введите строку для поиска в описании: ")
    transactions = search_by_description(transactions, search_query)

    print("\nРаспечатываю итоговый список транзакций...")
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия.")
    else:
        print(f"Всего операций для вывода: {len(transactions)}")
        for t in transactions:
            date = t.get('date', 'Нет даты')
            desc = t.get('description', 'Нет описания')
            amount = t.get('operationAmount', {}).get('amount', '0')

            # Маскировка
            from_info = t.get('from', 'Неизвестно')
            if 'Счет' in from_info:
                masked_from = get_mask_account(from_info)
            else:
                masked_from = get_mask_card_number(from_info)

            print(f"{date} | {desc} | {masked_from} | Сумма: {amount}")


if __name__ == "__main__":
    main()