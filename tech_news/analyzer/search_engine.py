from tech_news.database import search_news
import datetime

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
    response_tuple = []
    try:
        # source of the code use in the line 26
        # https://stackoverflow.com/questions/16870663/how-do-i-validate-a-
        # date-string-format-in-python/16870699
        datetime.datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida")
    response = search_news({"timestamp": {"$regex": date}})
    for date in response:
        tuple_value = [date["title"], date["url"]]
        respose_data = tuple(tuple_value)
        response_tuple.append(respose_data)
    return response_tuple


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
