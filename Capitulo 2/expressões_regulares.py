import requests
from bs4 import BeautifulSoup
import re

html = requests.get('https://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.content, 'html.parser')

images = bs.find_all('img', {'src': re.compile('\.\.\/img\/gifts/img.*\.jpg')})

#Exibe somente os Paths relativo das imagens
for image in images:
    print(image['src'])