from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    # referencia:
    # https://nilsoncunha.github.io/portfolioweb/comandos-uteis-em-mongodb-e-python/
    filter_title = {"title": {"$regex": title, "$options": "i"}}
    list_news = search_news(filter_title)

    news_filtred = []
    for news in list_news:
        news_filtred.append((news["title"], news["url"]))

    return news_filtred


# Requisito 8
def search_by_date(date):
    pass


# Requisito 9
def search_by_category(category):
    filter_category = {"category": {"$regex": category, "$options": "i"}}
    list_news = search_news(filter_category)

    news_filtred = []
    for news in list_news:
        news_filtred.append((news["title"], news["url"]))

    print(news_filtred)
    return news_filtred
