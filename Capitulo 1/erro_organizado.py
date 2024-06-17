import requests
from requests import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = requests.get(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.content, 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('https://pythonscraping.com/pages/page1.html')      

if title == None:
    print('Título não foi encontrado')
else:
    print(title)  