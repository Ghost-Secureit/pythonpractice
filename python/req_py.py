import requests

r = requests.get('https://news.ycombinator.com/newest')
header = r.head()
json = r.json()

print(header,json)