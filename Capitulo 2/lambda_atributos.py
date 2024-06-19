import requests
from bs4 import BeautifulSoup
import re

html = requests.get('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.content, 'html.parser')

#Pegando o(s) atributo, com função lambda
tags = bs.find_all(lambda tag: tag.get_text() == 'Or maybe he\'s only resting?')
print(tags)