import pytest

from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number(return_card_number):
    assert get_mask_card_number("1234567890123456") == return_card_number

@pytest.mark.parametrize("input_card_number_length, return_card_number_length", [("123456789012345678", "1234 56** **** 5678"), ("", " ** **** ")])
def test_get_mask_card_number_length(input_card_number_length, return_card_number_length):
    assert get_mask_card_number(input_card_number_length) == return_card_number_length