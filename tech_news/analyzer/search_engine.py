from tech_news.database import search_news
from datetime import datetime


def search_by_title(title):
    # referencia:
    # https://nilsoncunha.github.io/portfolioweb/comandos-uteis-em-mongodb-e-python/
    filter_title = {"title": {"$regex": title, "$options": "i"}}
    list_news = search_news(filter_title)

    news_filtred = []
    for news in list_news:
        news_filtred.append((news["title"], news["url"]))

    return news_filtred


def search_by_date(date):
    try:
        d = datetime.strptime(date, "%Y-%m-%d")
        new_date = d.strftime("%d/%m/%Y")
        filter_date = {"timestamp": new_date}
        list_news = search_news(filter_date)

        news_filtred = []
        for news in list_news:
            news_filtred.append((news["title"], news["url"]))
    except ValueError:
        raise (ValueError("Data inválida"))

    return news_filtred


def search_by_category(category):
    filter_category = {"category": {"$regex": category, "$options": "i"}}
    list_news = search_news(filter_category)

    news_filtred = []
    for news in list_news:
        news_filtred.append((news["title"], news["url"]))

    return news_filtred
