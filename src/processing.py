import re
from collections import Counter
from typing import Any, Dict, List


def filter_by_state(list_of_transactions: list[dict], transaction_state: str = "EXECUTED") -> list[dict]:
    """Функция возвращает новый список словарей, у которых ключ state соответствует указанному значению"""
    new_list_of_transactions = []
    for transaction in list_of_transactions:
        if transaction.get("state") == transaction_state:
            new_list_of_transactions.append(transaction)
    return new_list_of_transactions


def sort_by_date(list_of_transactions: list[dict], sort_in_descending_order: bool = True) -> list[dict]:
    """Функция возвращает новый список, отсортированный по дате"""
    sorted_transactions = sorted(
        list_of_transactions, key=lambda transaction: transaction["date"], reverse=sort_in_descending_order
    )
    return sorted_transactions


def filter_by_description(transactions: List[Dict[str, Any]], search_string: str) -> List[Dict[str, Any]]:
    """Ищет транзакции, в описании которых содержится заданная строка поиска."""
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [transaction for transaction in transactions if pattern.search(transaction.get("description", ""))]


def count_transactions_by_category(transactions: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает количество транзакций для каждой категории на основе описаний транзакций."""
    categories_lower = [category.lower() for category in categories]
    categories_used = []
    for transaction in transactions:
        description = transaction.get("description", "").lower()
        for category in categories_lower:
            if category in description:
                categories_used.append(category)
    # Преобразование категорий обратно в исходный регистр и возвращение результата
    return Counter([categories[categories_lower.index(category)] for category in categories_used])
