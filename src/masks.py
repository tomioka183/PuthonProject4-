def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты в формате 7000 79** **** 6361"""
    if card_number.isdigit() and len(card_number) == 16:
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    return "Некорректный номер карты"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер счета в формате **4305"""
    if account_number.isdigit() and len(account_number) >= 4:
        return f"**{account_number[-4:]}"
    return "Некорректный номер счета"
