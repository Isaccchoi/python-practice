import requests
from bs4 import BeautifulSoup

webtoon_url = "http://comic.naver.com/webtoon/list.nhn?titleId=651673"

source = requests.get(webtoon_url)
soup = BeautifulSoup(source.text, 'lxml')
# print(soup.prettify())

with open('sample.txt', 'wt') as f:
    f.write(soup.prettify())
