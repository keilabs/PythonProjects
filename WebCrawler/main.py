import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        if page is 1:
            url = 'http://www.mangahere.co/latest/'
        else:
            url = 'http://www.mangahere.co/latest/' + str(page)

        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, "html.parser")
        for link in soup.findAll('a', {'class': 'manga_info'}):   #loop through the source code and find all links with class manga_info.
            title = link.string
            href = link.get('href')
            print(href)
            print(title)
            get_single_item_data(href)
        page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.findAll('p', {'id': 'hide', 'class': 'clearfix'}):
        print(item_name.string)

trade_spider(3)