import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlopen
import re
import random

visited = set()  # Conjunto para armazenar URLs visitadas

def getInternalLinks(bsObj, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []
    for link in bsObj.findAll('a', href=re.compile('^(/|.*' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if link.attrs['href'].startswith('/'):
                    internalLinks.append(includeUrl + link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    for link in bsObj.findAll('a', href=re.compile('^(http|www)((?!' + excludeUrl + ').)*$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLink(startingPage):
    try:
        html = requests.get(startingPage)
        bsObj = BeautifulSoup(html.content, 'html.parser')
        externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
        if len(externalLinks) == 0:
            internalLinks = getInternalLinks(bsObj, startingPage)
            if len(internalLinks) == 0:
                return None  # Nenhum link interno ou externo encontrado
            else:
                # Tenta novamente com um link interno aleatório
                return getRandomExternalLink(internalLinks[random.randint(0, len(internalLinks) - 1)])
        else:
            return externalLinks[random.randint(0, len(externalLinks) - 1)]
    except Exception as e:
        print(f"Erro ao obter links de {startingPage}: {e}")
        return None

def followExternalOnly(startingSite):
    global visited
    while True:
        externaLink = getRandomExternalLink(startingSite)
        if externaLink is None:
            print(f"Nenhum link externo encontrado a partir de {startingSite}")
            break
        if externaLink in visited:
            print(f"Link já visitado: {externaLink}")
            continue
        visited.add(externaLink)
        print("Seguindo link externo: " + externaLink)
        startingSite = externaLink

# Chamada inicial da função
#followExternalOnly('http://oreilly.com')

'''se seu objetivo é rastrear um site todo em
busca de links externos e tomar nota de cada um deles, a seguinte função
pode ser acrescentada:

              |
              |
              |
              V                                                           '''

# Coleta uma lista de todos os URLs externos encontrados no site
allExtLinks = set()
allIntLinks = set()

def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    domain = '{}://{}'.format(urlparse(siteUrl).scheme,urlparse(siteUrl).netloc)
    bs = BeautifulSoup(html, 'html.parser')

    internalLinks = getInternalLinks(bs, domain)
    externalLinks = getExternalLinks(bs, domain)

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks(link)

allIntLinks.add('http://oreilly.com')
getAllExternalLinks('http://oreilly.com')