import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.content, 'html.parser')

for child in bs.find('table', id='giftList').children: #Obtendo apenas o Filho(Logo abaixo do Pai), sem os decendentes
    print(child)