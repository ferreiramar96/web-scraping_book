import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.content, 'html.parser')

nameList = bs.find_all('span', class_='green')
#Find_all retorna uma lista de Tags

for name in nameList:
    print(name.get_text())



'''Podemos utilizar:
    .find_all(['h1', 'h2', 'h3', 'h4']) --> Passar uma lista de tags
    
   Podemos também:
    .find_all('span', {'class': {'green', 'red'}})
    
    PARÂMETROS: 
    recursive --> analisa os filhos e os filhos dos filhos'''