import os

import requests
from dotenv import load_dotenv

# Загрузка переменных из .env-файла
load_dotenv()

API_KEY = os.getenv("API_KEY")


def amount_transaction_in_rubles(transaction):
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях.
    Если транзакция была в USD или EUR происходит конвертация суммы операции в рубли."""

    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?from={currency}&to=RUB&amount={amount}"
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data.get("success") and "result" in data:
                return float(data["result"])
