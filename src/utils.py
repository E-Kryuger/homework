import json
import os


def list_from_json(path_to_file):
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""

    if not os.path.exists(path_to_file):
        return []

    try:
        with open(path_to_file) as file:
            transactions_info = json.load(file)
            if isinstance(transactions_info, list):
                return transactions_info
            else:
                return []

    except (json.JSONDecodeError, IOError):
        return []
