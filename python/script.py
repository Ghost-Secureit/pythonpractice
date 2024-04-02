import requests
from bs4 import BeautifulSoup

data = requests.get('https://news.ycombinator.com/')
so = BeautifulSoup(data.text, 'html.parser')
links = so.select('.title')

print(links)