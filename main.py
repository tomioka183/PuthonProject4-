import os

from src.processing import filter_by_state, process_bank_search, sort_by_date
# Импортируем твои функции из папки src
from src.utils import read_financial_transactions_json
from src.widget import get_date, mask_account_card  # функции маскировки и даты


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    choice = input("\nПользователь: ")

    # 1. Загрузка данных
    # ВАЖНО: Убедись, что файл operations.json лежит в папке data
    file_path = os.path.join("data", "operations.json")

    if choice == "1":
        print("Программа: Для обработки выбран JSON-файл.")
        transactions = read_financial_transactions_json(file_path)
    elif choice in ["2", "3"]:
        print("Программа: Форматы CSV и XLSX будут доступны в следующих версиях.")
        return
    else:
        print("Программа: Неверный выбор.")
        return

    # 2. Фильтрация по статусу
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status_input = input(f"\nВведите статус, по которому необходимо выполнить фильтрацию.\n"
                             f"Доступные для фильтровки статусы: {', '.join(valid_statuses)}\n"
                             "Пользователь: ").strip().upper()

        if status_input in valid_statuses:
            transactions = filter_by_state(transactions, status_input)
            print(f'Программа: Операции отфильтрованы по статусу "{status_input}"')
            break
        else:
            print(f'Программа: Статус операции "{status_input}" недоступен.')

    # 3. Сортировка по дате
    is_sort = input("\nОтсортировать операции по дате? Да/Нет\nПользователь: ").lower()
    if is_sort == "да":
        order = input("Отсортировать по возрастанию или по убыванию?\nПользователь: ").lower()
        is_reverse = True if order == "по убыванию" else False
        transactions = sort_by_date(transactions, is_reverse)

    # 4. Фильтрация по валюте
    is_rub = input("\nВыводить только рублевые транзакции? Да/Нет\nПользователь: ").lower()
    if is_rub == "да":
        transactions = [
            t for t in transactions
            if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"
        ]    # 5. Фильтрация по слову в описании (Регулярные выражения)
    is_filter_desc = input("\nОтфильтровать список транзакций по определенному слову в описании? Да/Нет\n"
                           "Пользователь: ").lower()
    if is_filter_desc == "да":
        search_query = input("Введите слово для поиска: ")
        transactions = process_bank_search(transactions, search_query)

    # 6. Финальный вывод
    print("\nРаспечатываю итоговый список транзакций...")

    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {len(transactions)}\n")

        for op in transactions:
            # Превращаем дату в формат 08.12.2019
            date_formatted = get_date(op.get("date", ""))
            description = op.get("description", "Без описания")

            # Маскируем номера карт и счетов
            from_info = op.get("from")
            to_info = op.get("to", "")

            # Если есть отправитель, маскируем его
            if from_info:
                sender = mask_account_card(from_info)
                receiver = mask_account_card(to_info)
                route = f"{sender} -> {receiver}"
            else:
                route = mask_account_card(to_info)

            amount = op.get("operationAmount", {}).get("amount")
            currency = op.get("operationAmount", {}).get("currency", {}).get("name")

            print(f"{date_formatted} {description}")
            print(route)
            print(f"Сумма: {amount} {currency}\n")

if __name__ == "__main__":
    main()