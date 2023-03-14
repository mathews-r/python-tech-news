from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    news = find_news()

    categories = []
    for category in news:
        categories.append(category["category"])

    sorted_categories = Counter(sorted(categories)).most_common()

    new_categories = []
    for category in sorted_categories[0:5]:
        new_categories.append(category[0])

    return new_categories


top_5_categories()
