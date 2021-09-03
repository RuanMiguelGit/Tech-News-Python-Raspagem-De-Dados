from parsel import Selector
from tech_news.database import create_news
from tech_news.validate_news import writers, comments, shares
import requests
import time


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    if response.status_code == 200:
        return response.text
    else:
        return None


# a

# Requisito 2
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    response = Selector(html_content)
    url = response.css("head link[rel=canonical]::attr(href)").get()
    source = response.css("div.z--mb-16 > div > a::text").getall()
    title = response.css("#js-article-title ::text").get()
    timestamp = response.css("#js-article-date::attr(datetime)").get()
    writer = response.css(
        "p.z--m-none.z--truncate.z--font-bold > a::text"
    ).get()
    shares_count = response.css(".tec--toolbar__item::text").get()
    comments_count = response.css("#js-comments-btn::attr(data-count)").get()
    sources = [s.strip() for s in source]
    categories = response.css("a.tec--badge--primary ::text").getall()
    categoriess = [s.strip() for s in categories]
    summarys = response.css(
        "div.tec--article__body > p:nth-child(1) *::text"
    ).getall()
    summary = "".join(summarys)
    obj = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writers(writer),
        "shares_count": shares(shares_count),
        "comments_count": comments(comments_count),
        "summary": summary,
        "sources": sources,
        "categories": categoriess,
    }
    return obj


# Requisito 3
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    response = Selector(html_content)
    response_links = response.css(
        "div.tec--list__item > article > div > h3 > a::attr(href)"
    ).getall()
    return response_links


# Requisito 4
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    response = Selector(html_content)
    reponse_next_page = response.css(
        "div.z--col.z--w-2-3 > div.tec--list.tec--list--lg > a ::attr(href)"
    ).get()
    return reponse_next_page


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    list_of_news = []
    page_url = "https://www.tecmundo.com.br/novidades"
    while amount >= len(list_of_news):
        response = fetch(page_url)
        respose_list_of_urls = scrape_novidades(response)
        for news in respose_list_of_urls:
            list_of_news.append(scrape_noticia(fetch(news)))
            if len(list_of_news) == amount:
                create_news(list_of_news)
                return list_of_news
        page_url = scrape_next_page_link(response)
