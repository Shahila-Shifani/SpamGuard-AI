import re

def clean_message(message):
    """Lowercase text and replace repeated whitespace with a single space."""
    message = str(message).lower()
    message = re.sub(r"http\S+|www\.\S+", " URL ", message)
    message = re.sub(r"\s+", " ", message)
    return message.strip()
