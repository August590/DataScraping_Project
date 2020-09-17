import requests
from bs4 import BeautifulSoup
import pprint

url = 'https://news.ycombinator.com/news'
hn = []
# res = requests.get(f'https://news.ycombinator.com
# /news')

# print(res.text)
# soup = BeautifulSoup(res.text, 'html.parser')

# links = soup.select('.storylink')
# subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    for inx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[inx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points >= 100:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


def pageLooping(url, num_pages):
    i = 1
    hnDict = {}
    while i <= num_pages:
        res = requests.get(f'{url}?p={i}')
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select('.storylink')
        subtext = soup.select('.subtext')
        hnDict = create_custom_hn(links, subtext)
        i += 1
    return hnDict


pprint.pprint(pageLooping(url, 2))
# pprint.pprint(create_custom_hn(links, subtext))
