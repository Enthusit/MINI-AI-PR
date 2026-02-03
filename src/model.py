def predict(text: str) -> str:
    if "good" in text:
        return "positive"
    elif "bad" in text:
        return "negative"
    return "neutral"
