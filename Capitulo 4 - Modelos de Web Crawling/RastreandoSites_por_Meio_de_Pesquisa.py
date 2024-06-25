import requests
from bs4 import BeautifulSoup

class Content:
    """Classe-base comum para todos os artigos/páginas"""
    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.title = title
        self.body = body
        self.url = url # --> Acrescentamos apropriedade URL para manter o 
                       #controle dos lugares em que o conteúdo foi encontrado

    def print(self):
        """Uma função flexível de exibição controla a saída"""
        print("New article found for topic: {}".format(self.topic))
        print("TITLE: {}".format(self.title))
        print("BODY:\n{}".format(self.body))
        print("URL: {}".format(self.url))

class Website:
    """Contém informações sobre a estrutura do site"""
    def __init__(self, name, url, searchUrl, resultListing,
        resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl # --> local a ser acessado para obter os resultados de pesquisa
                                   #se o tópico que estiver procurando for concatenado.
        self.resultListing = resultListing # --> a “caixa” que contém as informações de cada resultado
        self.resultUrl = resultUrl # --> a tag dentro dessa caixa, que fornecerá o URL exato do resultado
        self.absoluteUrl=absoluteUrl # --> é um booleano que informa se esses resultados de busca são URLs absolutos ou relativos
        self.titleTag = titleTag
        self.bodyTag = bodyTag

class Crawler:
    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')
    
    def safeGet(self, pageObj, selector):
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj) > 0:
            return childObj[0].get_text()
        return ""
    
    def search(self, topic, site):
        """Pesquisa um dado site em busca de um dado tópico e registra
        todas as páginas encontradas"""
        bs = self.getPage(site.searchUrl + topic)
        searchResults = bs.select(site.resultListing)
        for result in searchResults:
            url = result.select(site.resultUrl)[0].attrs["href"]
            # Verifica se é um URL relativo ou absoluto
            if(site.absoluteUrl):
                bs = self.getPage(url)
            else:
                bs = self.getPage(site.url + url)
            if bs is None:
                print("Something was wrong with that page or URL. Skipping!")
                return
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(topic, title, body, url)
                content.print()


crawler = Crawler()
siteData = [['O\'Reilly Media', 'http://oreilly.com',
'https://ssearch.oreilly.com/?q=','article.product-result',
'p.title a', True, 'h1', 'section#product-description'],
['Reuters', 'http://reuters.com',
'http://www.reuters.com/search/news?blob=',
'div.search-result-content','h3.search-result-title a',
False, 'h1', 'div.StandardArticleBody_body_1gnLA'],
['Brookings', 'http://www.brookings.edu',
'https://www.brookings.edu/search/?s=',
'div.list-content article', 'h4.title a', True, 'h1',
'div.post-body']]
sites = []
for row in siteData:
    sites.append(Website(row[0], row[1], row[2],
    row[3], row[4], row[5], row[6], row[7]))

topics = ['python', 'data science']
for topic in topics:
    print("GETTING INFO ABOUT: " + topic)
    for targetSite in sites:
        crawler.search(topic, targetSite)