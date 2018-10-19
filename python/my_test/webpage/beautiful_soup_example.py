# beautifulsoup4
from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
# soup = BeautifulSoup(open("index.html"))

soup = BeautifulSoup(html_doc)
# print(soup.prettify())
# soup.find_all("a")

if __name__ == '__main__':
    from minitest import *

    with test("find_all"):
        all_a = soup.find_all("a")
        filter(lambda a: a.attrs["id"]=="link3", all_a).pp()
        soup.find(id="link3").pp()
