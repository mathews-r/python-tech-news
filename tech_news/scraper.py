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
    soup = BeautifulSoup(html_content, "html.parser")

    url = soup.find("link", rel="canonical").get("href")
    title = soup.find("h1", class_="entry-title").text.strip()
    timestamp = soup.find("li", class_="meta-date").text
    writer = soup.find("a", class_="url fn n").text
    reading_time = soup.find("li", class_="meta-reading-time").text[:2]
    summary = soup.find_all("p")[0].text.strip()
    category = soup.find("span", class_="label").text
    # print(summary)

    dict_news = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time),
        "summary": summary,
        "category": category,
    }
    # print(dict_news)
    return dict_news


# Requisito 5
def get_tech_news(amount):
    pass


blog = "https://blog.betrybe.com/linguagem-de-programacao/o-que-e-array/"
empowerment = (
    "https://blog.betrybe.com/carreira/empowerment-lideranca-o-que-e/"
)

# html = fetch(blog)
html = fetch(empowerment)
scrape_news(html)
