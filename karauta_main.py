from bs4 import BeautifulSoup
import requests
from xlsx import KExcel


def main(link, name):
    print("Паршу " + name + " :-- " + link)
    if link.find("?") != -1:
        link += "&"
    else:
        link += "?"
    products_id = []

    r = requests.get("{}page=1".format(link), headers={
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
    })
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        pages = (soup.find("div", attrs={"class": "pagination-top"}).find("span").getText()).replace("/ ", "")\
            .replace(" ", "")
    except AttributeError:
        pages = 1
    pages = int(pages)

    print(pages)
    for i in range(1, pages+1):
        r = requests.get("{}page={}".format(link, i), headers={
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
        })
        soup = BeautifulSoup(r.text, 'html.parser')
        product_links = soup.find_all("a", attrs={"class": "product-card"})
        print(product_links)
        # Цены в API не получаются (ошибки 500 503), поэтому беру отсюда. попытки в 123.py
        for product_link in product_links:
            products_id.append(product_link["href"].split("/")[-1])
    print(len(products_id))
    writer = KExcel("output_{}.xlsx".format(name), products_id)
    writer.save()
    print("output_{}.xlsx".format(name) + " сохранён!")

