import requests
from bs4 import BeautifulSoup


res = requests.get('https://news.ycombinator.com/newest')
res2 = requests.get('https://news.ycombinator.com/newest?next=39787290&n=31')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.title')
links2 = soup2.select('.title')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

mega_links = links+links2
mega_subtext = subtext+subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist,key=lambda k:k['votes'], reversed=True)


def create_custom_hn(links, subtext):
    min_length = min(len(links), len(subtext))
    hn = []
    for idx in range(min_length):
        item = links[idx]
        title = item.getText()
        href = item.get('href') 
        vote = subtext[idx].select('.score')
        if vote:
            points_text = vote[0].getText().replace(' points', '')
            points = int(points_text) if points_text.isdigit() else 0
            hn.append({'title': title, 'link': href, 'votes': points})
        else:
            hn.append({'title': title, 'link': href, 'votes': 0})
    return hn

print(create_custom_hn(mega_links, mega_subtext))

