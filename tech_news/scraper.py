# from bs4 import BeautifulSoup
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
    pass


# Requisito 3
def scrape_next_page_link(html_content):
    pass


# Requisito 4
def scrape_news(html_content):
    pass


# Requisito 5
def get_tech_news(amount):
    pass
