import requests
from bs4 import BeautifulSoup
from src.news import URL_NEWS


def get_news() -> str:
    r = requests.get(URL_NEWS, verify=False)
    soup = BeautifulSoup(r.text, "html.parser")
    item = soup.find_all("item")
    items = []
    count = 0
    for i in item:
        if count == 3:
            break
        count += 1
        i = clean_item(str(i))
        items.append(i)
    return items


def clean_item(item: str) -> str:
    item = item.replace("<item><title>", "")
    item = item.replace("</item>", "")
    item = item.split("-")
    return item[0]


# if __name__ == "__main__":
#     print(get_news())
