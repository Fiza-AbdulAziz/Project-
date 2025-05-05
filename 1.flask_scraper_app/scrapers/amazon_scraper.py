# amazon_scraper.py
import requests
from bs4 import BeautifulSoup

def get_amazon_data(query):
    search_url = f"https://www.amazon.com/s?k={query.replace(' ', '+')}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')

    results = []
    for product in soup.select('.s-result-item')[:5]:
        title = product.h2.text if product.h2 else "No Title"
        link = "https://www.amazon.com" + product.h2.a['href'] if product.h2 and product.h2.a else "#"
        results.append({"title": title.strip(), "link": link})
    return results
