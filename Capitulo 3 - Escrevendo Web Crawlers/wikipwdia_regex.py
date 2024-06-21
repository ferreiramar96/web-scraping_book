import requests
from bs4 import BeautifulSoup
import re

html = requests.get('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html.content, 'html.parser')

for link in bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link.attrs:
        print(link.attrs['href'])