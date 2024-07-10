import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(return_card_number):
    assert get_mask_card_number("1234567890123456") == return_card_number


@pytest.mark.parametrize(
    "input_card_number_length, return_card_number_length",
    [("123456789012345678", "1234 56** **** 5678"), ("", " ** **** ")],
)
def test_get_mask_card_number_length(input_card_number_length, return_card_number_length):
    assert get_mask_card_number(input_card_number_length) == return_card_number_length


@pytest.mark.parametrize(
    "input_get_mask_account, return_get_mask_account",
    [("123456789012345678", "**5678"), ("", "**"), ("123456789", "**6789"), ("73654108430135874305", "**4305")],
)
def test_get_mask_account(input_get_mask_account, return_get_mask_account):
    assert get_mask_account(input_get_mask_account) == return_get_mask_account
