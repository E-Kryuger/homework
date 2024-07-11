import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "input_account_card, return_mask_account_card",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счёт 73654108430135874305", "Счёт **4305"),
        ("", " ** **** "),
    ],
)
def test_mask_account_card(input_account_card, return_mask_account_card):
    assert mask_account_card(input_account_card) == return_mask_account_card


@pytest.mark.parametrize(
    "input_datetime_str, return_new_format_date",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2023-01-01T08:06:00.123456", "01.01.2023"),
    ],
)
def test_get_date(input_datetime_str, return_new_format_date):
    assert get_date(input_datetime_str) == return_new_format_date
