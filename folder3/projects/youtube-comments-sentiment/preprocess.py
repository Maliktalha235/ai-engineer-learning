import re
import html

def clean_text(text):
    text = html.unescape(text)
    # Removing urls
    text = re.sub(r"http\S+|www\S+", "", text)
    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text