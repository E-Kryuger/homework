from datetime import datetime


def mask_account_card(type_and_number: str) -> str:
    """Обрабатывает информацию о картах и о счетах"""
    if type_and_number[:4].lower() in ["счет", "счёт"]:
        return f"{type_and_number[:4].title()} **{type_and_number[-4:]}"
    else:
        return f"{type_and_number[:-12]} {type_and_number[-12:-10]}** **** {type_and_number[-4:]}"


def get_date(datetime_str: str) -> str:
    """Меняет формат даты с datetime на привычный ДД.ММ.ГГГГ"""
    datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%f")
    new_format_date = datetime_obj.strftime("%d.%m.%Y")
    return new_format_date
