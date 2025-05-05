import requests
from bs4 import BeautifulSoup
def get_youtube_data(query):
    search_url=f"https://www.youtube.com/results?search_query={query.replace('','+')}"
    headers={"User-Agent": "Mozilla/5.0"}
    response=requests.get(search_url,headers=headers)
    soup=BeautifulSoup(response.text,"html.parser")
    results=[]
    for script in soup.find_all("script"):
        if 'var ytInitialData' in script.text:
            # YouTube has obfuscated this — recommend using Selenium instead for real data
            return [{"title": "YouTube blocks scraping. Use API or Selenium.", "link": "#"}]
    return results