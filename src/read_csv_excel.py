import logging
import os

import pandas as pd

logger = logging.getLogger("read_csv_excel")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/read_csv_excel.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_transactions_csv(path_to_file):
    """Читает CSV-файл и возвращает список словарей с данными о финансовых транзакциях."""

    if not os.path.exists(path_to_file):
        logger.warning(f"Указан несуществующий путь: {path_to_file}")
        return []

    df = pd.read_csv(path_to_file, delimiter=";")
    return df.to_dict(orient="records")


def read_transactions_excel(path_to_file):
    """Читает Excel-файл и возвращает список словарей с данными о финансовых транзакциях."""

    if not os.path.exists(path_to_file):
        logger.warning(f"Указан несуществующий путь: {path_to_file}")
        return []

    df = pd.read_excel(path_to_file)
    return df.to_dict(orient="records")
