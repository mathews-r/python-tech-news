from bs4 import BeautifulSoup
import requests
import time


headers = {"User-Agent": "Fake user-agent"}
base_url = "https://blog.betrybe.com/"


# Requisito 1
def fetch(url: str):
    try:
        response = requests.get(url, headers=headers)
        time.sleep(1)
        response.raise_for_status()

    except (requests.HTTPError, requests.ReadTimeout):
        return None

    return response.text


# Requisito 2
def scrape_updates(html_content):
    soup = BeautifulSoup(html_content, "html.parser")

    news_list = []
    for news in soup.find_all("a", class_="cs-overlay-link"):
        news_list.append(news.get("href"))
    return news_list


# Requisito 3
def scrape_next_page_link(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    next_page = soup.find("a", class_="next page-numbers")

    if next_page is None:
        return None

    return next_page.get("href")


# Requisito 4
def scrape_news(html_content):
    pass


# Requisito 5
def get_tech_news(amount):
    pass


html = fetch(base_url)
scrape_next_page_link(
    '<span aria-current="page" class="page-numbers current">80</span>'
)
