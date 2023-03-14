from tech_news.database import find_news


# Requisito 10
def top_5_categories():
    news = find_news()

    categories = []
    for category in news:
        if category["category"] not in news:
            categories.append(category["category"])
        else:
            True
    print(categories)
    return categories


top_5_categories()
