import re
import time
from typing import Iterator
import requests
import lxml.html
from pymongo import MongoClient

def main():
    """
    クローラーのメインの処理
    """
    client = MongoClient('localhost', 27017)
    collection = client.scraping.ebooks
    collection.create_index('key', unique=True)

    session = requests.Session()
    response = requests.get('https://gihyo.jp/dp')
    urls = scrape_list_page(response)

    for url in urls:
        key = extract_key(url)

        ebook = collection.find_one({'key': key})
        if not ebook:
            time.sleep(1)
            response = session.get(url)
            ebook = scrape_detail_page(response)
            collection.insert_one(ebook)

        print(ebook)


def scrape_list_page(response: requests.Response) -> Iterator[str]:
    """
    一覧ページのResponseから詳細ページのURLを抜き出すジェネレーター関数。
    """
    html = lxml.html.fromstring(response.text)
    html.make_links_absolute(response.url)

    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
        url = a.get('href')
        yield url

def scrape_detail_page(response: requests.Response) -> dict:
    """
    一覧ページのResponseから電子書籍の情報をDictで取得する。
    """
    html = lxml.html.fromstring(response.text)
    ebook = {
        'url': response.url,
        'key': extract_key(response.url),
        'title': html.cssselect('#bookTitle')[0].text_content(),
        'price': html.cssselect('.buy')[0].text.strip(),
        'content': [normalize_spaces(h3.text_content()) for h3 in html.cssselect('#content > h3')],
    }
    return ebook

def extract_key(url: str) -> str:
    """
    URLからキー(URLの末尾のISBN)を抜き出す
    """
    m = re.search(r'/([^/]+)$', url)
    return m.group(1)

def normalize_spaces(s: str) -> str:
    """
    連続する空白を1つのスペースに置き換え、前後の空白を削除した新しい文字列を取得する
    """
    return re.sub(r'\s+', ' ', s).strip()

if __name__ == '__main__':
    main()