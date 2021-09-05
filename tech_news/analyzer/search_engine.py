from tech_news.database import search_news

# import datetime

# Requisito 6


def search_by_title(title):
    """Seu código deve vir aqui"""
    response = search_news({"title": title.lower().capitalize()})
    response_tuple = []
    if len(response) == 0:
        return []
    else:
        for title in response:
            tuple_value = [title["title"], title["url"]]
            respose_data = tuple(tuple_value)
            response_tuple.append(respose_data)
        return response_tuple


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
