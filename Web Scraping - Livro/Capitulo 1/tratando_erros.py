import requests
from requests import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup

try:
    html = requests.get('http://pythonscraping.com/pages/page1.html')
except URLError as e:
    #Servidor não encontrado
    print('O servidor não foi encontrado!')
except HTTPError as e:
    print(e)
    #Devolve null, executa um break ou algum outro "Plano B"
else:
    print('Está em trabalho...')
    bs = BeautifulSoup(html.content, 'html.parser')
    print(bs.h1)