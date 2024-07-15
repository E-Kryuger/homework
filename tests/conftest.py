import pytest


@pytest.fixture
def return_card_number():
    return "1234 56** **** 3456"


@pytest.fixture
def return_card_number_generator():
    return ["9999 9999 9999 9999"]
