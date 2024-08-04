import json
import logging
import os

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def list_from_json(path_to_file):
    """Функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными о транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список."""

    if not os.path.exists(path_to_file):
        logger.warning(f"Указан несуществующий путь: {path_to_file}")
        return []

    try:
        with open(path_to_file) as file:
            transactions_info = json.load(file)
            if isinstance(transactions_info, list):
                logger.info(f"Файл успешно прочитан: {path_to_file}")
                return transactions_info
            else:
                logger.warning(f"Недопустимый формат данных в файле: {path_to_file}")
                return []

    except (json.JSONDecodeError, IOError) as e:
        logger.error(f"При прочтении файла: {path_to_file} произошла ошибка: {e}")
        return []
