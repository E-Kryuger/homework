from src.generators import filter_by_currency
from src.processing import filter_by_description, filter_by_state, sort_by_date
from src.read_csv_excel import read_transactions_csv, read_transactions_excel
from src.utils import list_from_json
from src.widget import get_date, mask_account_card


def main():
    print(
        """Привет! Добро пожаловать в программу работы
с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )

    while True:
        selected_file = input("\nВведите номер необходимого пункта: ").strip()
        if selected_file == "1":
            print("\nДля обработки выбран JSON-файл")
            transactions = list_from_json("data/operations.json")
            break
        elif selected_file == "2":
            print("\nДля обработки выбран CSV-файл")
            transactions = read_transactions_csv("data/transactions.csv")
            break
        elif selected_file == "3":
            print("\nДля обработки выбран XLSX-файл")
            transactions = read_transactions_excel("data/transactions_excel.xlsx")
            break
        else:
            print(
                """
Вы ввели неверное значение.
Пожалуйста, введите только цифру, соответствующую необходимому пункту меню"""
            )

    while True:
        print(
            """
Введите статус, по которому необходимо выполнить фильтрацию.
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"""
        )

        transaction_state = input("\nНеобходимый статус: ").strip().upper()
        if transaction_state in ["EXECUTED", "CANCELED", "PENDING"]:
            user_transactions = filter_by_state(transactions, transaction_state)
            print(f'\nОперации отфильтрованы по статусу "{transaction_state}"')
            break
        else:
            print(f'\nСтатус операции "{transaction_state}" недоступен.')

    while True:
        sort_transactions_by_date = input("\nОтсортировать операции по дате?\nДа/Нет: ").strip().lower()
        if sort_transactions_by_date not in {"да", "нет"}:
            print('Пожалуйста, введите "Да" или "Нет"')
        elif sort_transactions_by_date == "да":
            while True:
                sorting_order = (
                    input("\nОтсортировать по возрастанию или по убыванию?\nПорядок сортировки: ").strip().lower()
                )
                if sorting_order not in {"по возрастанию", "по убыванию"}:
                    print('\nПожалуйста, введите "по возрастанию" или "по убыванию"')
                else:
                    user_transactions = sort_by_date(user_transactions, sorting_order == "по убыванию")
                    break
            break
        else:
            break
    while True:
        need_to_filter_by_currency = input("\nВыводить только рублевые транзакции?\nДа/Нет: ").strip().lower()
        if need_to_filter_by_currency == "да":
            user_transactions = list(filter_by_currency(user_transactions, "RUB"))
            break
        elif need_to_filter_by_currency == "нет":
            break
        else:
            print('Пожалуйста, введите "Да" или "Нет"')

    while True:
        need_filter_by_description = (
            input("\nОтфильтровать список транзакций по определенному слову в описании?\nДа/Нет: ").strip().lower()
        )
        if need_filter_by_description == "да":
            search_string = input("\nПо какому слову в описании будем фильтровать транзакции?: ")
            user_transactions = filter_by_description(user_transactions, search_string)
            break
        elif need_filter_by_description == "нет":
            break
        else:
            print('Пожалуйста, введите "Да" или "Нет"')

    if not user_transactions:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print("\nРаспечатываю итоговый список транзакций...")
    print("\nВсего банковских операций в выборке:", len(list(user_transactions)))

    for transaction in transactions:
        print()
        date_str = transaction.get("date", "")
        if date_str:
            date = get_date(date_str)
        description = transaction.get("description", "")
        print(date, description)

        from_card_or_account = transaction.get("from", "")
        to_card_or_account = transaction.get("to", "")
        to_masked_card_or_account = mask_account_card(to_card_or_account)
        if from_card_or_account:
            from_masked_card_or_account = mask_account_card(from_card_or_account)
            print(from_masked_card_or_account, "->", to_masked_card_or_account)
        else:
            print(to_masked_card_or_account)

        amount = transaction.get("operationAmount")
        if amount:
            currency = amount.get("currency", {}).get("code", "")
            amount = amount.get("amount")
        else:
            amount = transaction.get("amount")
            currency = transaction.get("currency_name", "")
        print("Сумма", amount, currency)


if __name__ == "__main__":
    main()
