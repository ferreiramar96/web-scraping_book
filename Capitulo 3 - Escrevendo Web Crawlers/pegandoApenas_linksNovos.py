import requests
from bs4 import BeautifulSoup
import re
import sys

#Aumentando o limite de recursão
sys.setrecursionlimit(5000)

pages = set()
contagem = 0
def getLinks(url):
    global pages, contagem
    html = requests.get(f'http://en.wikipedia.org{url}')
    bs = BeautifulSoup(html.content, 'html.parser')

    #Encontrar todos os links
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        #Verifica se existe o atributo no link encontrado
        if 'href' in link.attrs:
            #Se o link não estiver em nosso Conjunto, ele é adicionado
            if link.attrs['href'] not in pages:
                #Encotramos uma nova pagina
                newPage = link.attrs['href']
                print(newPage)
                contagem+=1
                print(contagem)
                pages.add(newPage)
                #Ele vai pegar e entrar no link, para buscar mais links
                getLinks(newPage) #Aplicando a recursão

getLinks('')