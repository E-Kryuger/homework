def filter_by_state(list_of_transactions: list[dict], transaction_state: str = 'EXECUTED') -> list[dict]:
    """Функция возвращает новый список словарей, у которых ключ state соответствует указанному значению"""
    new_list_of_transactions = []
    for transaction in list_of_transactions:
        if transaction['state'] == transaction_state:
            new_list_of_transactions.append(transaction)
    print(new_list_of_transactions)
    return new_list_of_transactions

def sort_by_date(list_of_transactions: list[dict], sort_in_descending_order: bool = True) -> list[dict]:
    """Функция возвращает новый список, отсортированный по дате"""
    sorted_transactions = sorted(list_of_transactions, key=lambda transaction: transaction['date'], reverse=sort_in_descending_order)
    print(sorted_transactions)
    return sorted_transactions

