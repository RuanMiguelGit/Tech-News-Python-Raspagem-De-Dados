import requests
import time
from parsel import Selector


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
    sources = [s.strip() for s in source]
    categories = response.css("a.tec--badge--primary ::text").getall()
    categoriess = [s.strip() for s in categories]
    summarys = response.css(
        "div.tec--article__body > p:nth-child(1) *::text"
    ).getall()
    summary = "".join(summarys)
    obj = {
        "url": url,
        "title": response.css("#js-article-title ::text").get(),
        "timestamp": response.css("#js-article-date::attr(datetime)").get(),
        "writer": response.css(
            "p.z--m-none.z--truncate.z--font-bold > a::text"
        )
        .get()
        .strip(),
        "shares_count": int(
            response.xpath('//*[@id="js-author-bar"]/nav/div[1]/text()')
            .get()
            .split()[0]
        ),
        "comments_count": int(
            response.xpath('//*[@id="js-comments-btn"]/text()')
            .getall()[1]
            .split()[0]
        ),
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
