def clean_text(text: str) -> str:
    text = text.lower()
    text = text.replace(".", "").replace(",", "")
    return text
