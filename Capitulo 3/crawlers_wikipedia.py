import requests
from bs4 import BeautifulSoup

html = requests.get('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html.content, 'html.parser')

for link in bs.find_all('a'):
    if 'href' in link.attrs:
        print(link.attrs['href'])