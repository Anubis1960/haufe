import tensorflow as tf
import re
from nltk.corpus import stopwords
from nltk import word_tokenize
fn_model = tf.keras.models.load_model('model.keras')


def prep(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^a-zA-Z]", " ", text).strip()
    text = re.sub(r"  +", " ", text).strip()
    text = text.lower()
    words = word_tokenize(text)
    words = [w for w in words if w not in stopwords.words("english")]
    text = " ".join(words)
    return text


def check_content(title:str, text: str) -> str:
    text = prep(text)
    title = prep(title)
    content = f"<title>{title}</title> <text>{text}</text>"
    prediction = fn_model.predict(content)

    return prediction
