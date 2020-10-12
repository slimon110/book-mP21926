import requests
from bs4 import BeautifulSoup
url = 'https://kknews.cc/zh-tw/home/kx5p5v8.html'

html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')

photos = soup.find_all('img')
for photo in photos:
    if photo['src'].startswith('http'):
        print(photo['src'])
