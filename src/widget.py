from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Маскирует информацию о карте или счете."""
    parts = info.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if "Счет" in name:
        return f"{name} {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"
