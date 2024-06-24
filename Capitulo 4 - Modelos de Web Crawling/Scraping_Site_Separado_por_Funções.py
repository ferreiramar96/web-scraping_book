import requests
from bs4 import BeautifulSoup

class Content:
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

def getPage(url):
    req = requests.get(url)
    return BeautifulSoup(req.text, 'html.parser')

def scrapeNYTimes(url):
    bs = getPage(url)
    title_tag = bs.find("h1")
    if title_tag:
        title = title_tag.text
    else:
        title = 'No title found'
    lines = bs.find_all("p")
    if lines:
        body = '\n'.join([line.text for line in lines])
    else:
        body = 'No body found'
    return Content(url, title, body)

def scrapeBrookings(url):
    bs = getPage(url)
    title_tag = bs.find("h1")
    if title_tag:
        title = title_tag.text
    else:
        title = 'No title found'
    body_div = bs.find("div", {"class": "post-body"})
    if body_div:
        body = body_div.text
    else:
        body = 'No body found'
    return Content(url, title, body)

url = 'https://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/'

content = scrapeBrookings(url)
print('Title: {}'.format(content.title))
print('URL: {}\n'.format(content.url))
print(content.body)

url = 'https://www.nytimes.com/2018/01/25/opinion/sunday/silicon-valley-immortality.html'
content = scrapeNYTimes(url)
print('Title: {}'.format(content.title))
print('URL: {}\n'.format(content.url))
print(content.body)
