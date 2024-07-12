def filter_by_currency(transactions, code_transactions):
    """Функция возвращающая итератор, который поочередно выдает транзакции, где валюта соответствует заданной"""
    filtered_transactions = list(
        filter(
            lambda transaction: transaction.get("operationAmount").get("currency").get("code") == code_transactions,
            transactions,
        )
    )
    if len(filtered_transactions) > 0:
        return iter(filtered_transactions)
    else:
        return


def transaction_descriptions(transactions):
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start, stop=None):
    """Генератор, который выдает номера банковских карт"""
    cards_numbers = []

    if stop == None:
        stop = start

    for i in range(start, stop + 1):
        card_number = (16 - len(str(i))) * "0" + str(i)
        cards_numbers.append(f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[-4:]}")
    return iter(cards_numbers)