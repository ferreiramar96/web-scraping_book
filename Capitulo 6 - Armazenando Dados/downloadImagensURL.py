import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

html = requests.get('http://www.pythonscraping.com/')
bs = BeautifulSoup(html.content, 'html.parser')

imageLocation = bs.find('a', {'id': 'logo'}).find('img')['src']
urlretrieve(imageLocation, 'logo.jpg')

'''Este código funciona bem se for necessário fazer o download de apenas um
arquivo e você souber como ele se chama e qual a sua extensão. A maioria
dos scrapers, porém, não faz download de um só arquivo e dá o trabalho
por encerrado.'''