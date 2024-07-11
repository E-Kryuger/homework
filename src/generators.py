def filter_by_currency(transactions, code_transactions):
    """Функция возвращающая итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""
    filtered_transactions = list(filter(lambda transaction: transaction.get("operationAmount").get("currency").get("code") == code_transactions, transactions))
    if len(filtered_transactions) > 0:
        return iter(filtered_transactions)

def transaction_descriptions(transactions):
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction.get("description")

def card_number_generator(starting_value, final_value):
    """Генератор, который выдает номера банковских карт"""
    for i in range(starting_value, final_value+1):
        card_number = (16-len(str(i)))*"0"+str(i)
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"