from tech_news.database import find_news
from collections import Counter


def top_5_categories():
    news = find_news()

    categories = []
    for category in news:
        categories.append(category["category"])

    sorted_categories = []
    for category in Counter(sorted(categories)).most_common()[0:5]:
        sorted_categories.append(category[0])

    return sorted_categories
