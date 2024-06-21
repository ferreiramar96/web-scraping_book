import requests
from bs4 import BeautifulSoup

html = requests.get('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.content, 'html.parser')
print(bs.h1)