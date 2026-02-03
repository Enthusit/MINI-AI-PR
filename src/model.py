def predict(text: str) -> str:
    if "good" in text:
        return "positive"
    return "negative"
