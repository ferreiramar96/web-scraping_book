import requests
from bs4 import BeautifulSoup
import re
import sys

#Aumentando o limite de recursão
sys.setrecursionlimit(5000)

'''Os sets são uma coleção de itens desordenada, 
parcialmente imutável e que não podem conter elementos 
duplicados. Por ser parcialmente imutável, os sets possuem 
permissão de adição e remoção de elementos'''

pages = set()

def getLinks(url):
    global pages
    html = requests.get(f'http://en.wikipedia.org{url}', allow_redirects=True) #Permitindo o redirecionamento
    bs = BeautifulSoup(html.content, 'html.parser')

    try:
        print(bs.h1.get_text()) #Pega o título de cada pag
        print(bs.find(id='mw-content-text').find('p')) #Pega o 1º parágrafo da pag
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href']) #Se existir, pega o link para edição

    except AttributeError:
        print('Esta página está vazia! Continuando...')

    #Encontrar todos os links
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        #Verifica se existe o atributo no link encontrado
        if 'href' in link.attrs:
            #Se o link não estiver em nosso Conjunto, ele é adicionado
            if link.attrs['href'] not in pages:
                #Encotramos uma nova pagina
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                #Ele vai pegar e entrar no link, para buscar mais links
                getLinks(newPage) #Aplicando a recursão

getLinks('')


#UTILIZANDO UMA ALTERNATIVA A EXPRESSÃO REGULAR (REGEX)
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#Opção alternativa

'''# Encontrar todos os links
    for link in bs.find_all('a', href=True):
        if link['href'].startswith('/wiki/'):
            if link['href'] not in pages:
                newPage = link['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage) # Aplicando a recursão'''