from util.scrape import *
from util.model import *

def predict_url(url: str) -> dict:
    title, text = scrape_url(url)
    if text is None:
        return {"error": "Invalid URL"}
    prediction = check_content(title, text)

    return {"prediction": prediction}

