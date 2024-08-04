import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    mask_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    if len(card_number) != 16:
        logger.info(f"У карты с маской {mask_card} нестандартная длина номера карты")
    else:
        logger.info(f"Маска карты: {mask_card}")
    return mask_card


def get_mask_account(account: str) -> str:
    """Функцию маскировки номера банковского счета"""
    mask_account = f"**{account[-4:]}"
    logger.info(f"Маска банковского счета: {mask_account}")
    return mask_account
