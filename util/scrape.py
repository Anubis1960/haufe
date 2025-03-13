from bs4 import BeautifulSoup
import requests

def scrape_url(url: str) -> (str, str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    soup = BeautifulSoup(response.content, "html.parser")
    text = soup.get_text(separator=' ', strip=True)
    title = soup.find("title")
    return title, text