from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(info: str) -> str:
    """Маскирует номер карты или счета."""
    parts = info.split()
    number = parts[-1]
    name = " ".join(parts[:-1])

    if "Счет" in name:
        return f"{name} {get_mask_account(number)}"
    else:
        return f"{name} {get_mask_card_number(number)}"

def get_date(date_str: str) -> str:
    """Преобразует строку с датой в формат ДД.ММ.ГГГГ."""
    # Пример: "2024-03-11T02:26:18.671407" -> "11.03.2024"
    date_part = date_str.split("T")[0]
    year, month, day = date_part.split("-")
    return f"{day}.{month}.{year}"