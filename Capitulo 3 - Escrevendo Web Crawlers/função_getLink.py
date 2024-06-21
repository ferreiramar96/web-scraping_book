import requests
from bs4 import BeautifulSoup
import re
import datetime
import random

#random.seed(datetime.datetime.now())
def getLinks(articleURL):
    html = requests.get(f'http://en.wikipedia.org{articleURL}')
    bs = BeautifulSoup(html.content, 'html.parser')
    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$')) #Retorna uma lista

links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0: #Função infinita (recursiva)
    newArticle = links[random.randint(0, len(links)-1)].attrs['href'] #Escolhendo a posição aleatória de um item, e pegando o atributo "href"
    print(newArticle)
    links = getLinks(newArticle)
