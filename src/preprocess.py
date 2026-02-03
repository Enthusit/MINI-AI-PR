import re

def clean_text(text: str) -> str:
    """
    Lowercases and removes punctuation from input text.
    """
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text
